import netgen.gui
from ngsolve import *
from netgen.geom2d import *
import matplotlib.pyplot as plt
from netgen.csg import unit_cube
from ngsolve.la import EigenValues_Preconditioner

SetHeapSize(100*1000*1000)
mesh = Mesh(unit_cube.GenerateMesh(maxh=0.5))
fes = H1(mesh, order=8)

class SymmetricGS(BaseMatrix):
    def __init__ (self, smoother):
        super(SymmetricGS, self).__init__()
        self.smoother = smoother
    def Mult (self, x, y):
        y[:] = 0.0
        self.smoother.Smooth(y, x)
        self.smoother.SmoothBack(y,x)
    def Height (self):
        return self.smoother.height
    def Width (self):
        return self.smoother.height


def SolveProblem(h=0.5, p=1, levels=1,
                 condense = False,
                 precond="local"):
    """
    Solve Poisson problem on l refinement levels.
        h: coarse mesh size
        p: polynomial degree
        l: number of refinement levels
        precond: name of a built-in preconditioner
        condense: if true, perform static condensations
    OUTPUT:
        List of tuples of ndofs and iterations
    """

    #mesh = Mesh(unit_square.GenerateMesh(maxh=h))
    mesh = Mesh(unit_cube.GenerateMesh(maxh=h))
    fes = H1(mesh, order=p, dirichlet="bottom|left")

    u, v = fes.TnT()
    a = BilinearForm(fes, eliminate_internal=condense)
    a += SymbolicBFI(grad(u)*(grad(v)))
    f = LinearForm(fes)
    f += SymbolicLFI(1*v)
    gfu = GridFunction(fes)
    Draw (gfu)




    if precond != "gs" and precond != "blockjacobi":
        c = Preconditioner(a, precond) # 'Register' c to a BEFORE assembly

    steps = []

    for l in range(levels):
        if l > 0: mesh.Refine()
        fes.Update()
        a.Assemble()
        f.Assemble()
        gfu.Update()

        if precond == "gs":
            preJpoint = a.mat.CreateSmoother(fes.FreeDofs())
            c = SymmetricGS(preJpoint)

        if precond == "blockjacobi":
            blocks = []
            freedofs = fes.FreeDofs()
            for v in mesh.vertices:
                vdofs = set()
                for el in mesh[v].elements:
                    vdofs |= set(d for d in fes.GetDofNrs(el) if freedofs[d])
                blocks.append(vdofs)
            c = a.mat.CreateBlockSmoother(blocks)

        lams = EigenValues_Preconditioner(mat=a.mat, pre=c.mat)
        print("Condition: ")
        print(max(lams) / min(lams))
        # Conjugate gradient solver
        inv = CGSolver(a.mat, c.mat, maxsteps=1000)

        # Solve steps depend on condense
        if condense:
            f.vec.data += a.harmonic_extension_trans * f.vec
        gfu.vec.data = inv * f.vec
        if condense:
            gfu.vec.data += a.harmonic_extension * gfu.vec
            gfu.vec.data += a.inner_solve * f.vec
        steps.append ( (fes.ndof, inv.GetSteps()) )
        #inv.GetStep()
        Redraw ()
    return steps

#print(SolveProblem(precond="local"))
ps = []
rs = []
for p in range(1,10):
    r = SolveProblem(h=0.25, p=p, levels=1, condense=True,
                     precond="multigrid")
    ps.append(p)
    rs.append(r.copy())
    print ("p =",p,", res =",r)

for i in range(0, len(ps)):
    print("p =", ps[i], ", res =", rs[i])








