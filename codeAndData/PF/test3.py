import netgen.gui
from netgen.geom2d import *
import matplotlib.pyplot as plt
from ngsolve.la import EigenValues_Preconditioner
from ngsolve import *
from netgen.csg import *

SetHeapSize(100*1000*1000)


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



box = OrthoBrick(Pnt(-3, -3, -3), Pnt(3, 3, 3)).bc("outer")
magnet = Cylinder(Pnt(-1, 0, 0), Pnt(1, 0, 0), 0.3) * OrthoBrick(Pnt(-1, -3, -3), Pnt(1, 3, 3))
air = box - magnet

geo = CSGeometry()
geo.Add(air.mat("air").transp())
geo.Add(magnet.mat("magnet").maxh(1))
geo.Draw()
mesh = Mesh(geo.GenerateMesh(maxh=2, curvaturesafety=1))
mesh.Curve(3)

fes = HCurl(mesh, order=3, dirichlet="outer", nograds=True)
print("ndof =", fes.ndof)
u, v = fes.TnT()

from math import pi
mu0 = 4 * pi * 1e-7
mur = CoefficientFunction([1000 if mat == "magnet" else 1
                               for mat in mesh.GetMaterials()])

a = BilinearForm(fes)
a += SymbolicBFI(1 / (mu0 * mur) * curl(u) * curl(v) + 1e-8 / (mu0 * mur) * u * v)
c = Preconditioner(a, "local")

f = LinearForm(fes)
mag = CoefficientFunction((1, 0, 0)) * \
        CoefficientFunction([1 if mat == "magnet" else 0 for mat in mesh.GetMaterials()])
f += SymbolicLFI(mag * curl(v), definedon=mesh.Materials("magnet"))

with TaskManager():
    a.Assemble()
    f.Assemble()

lams = EigenValues_Preconditioner(mat=a.mat, pre=c.mat)
print("Condition: ")
print(max(lams) / min(lams))

gfu = GridFunction(fes)
with TaskManager():
    r = solvers.CG(sol=gfu.vec, rhs=f.vec, mat=a.mat, pre=c.mat)

Draw(gfu, mesh, "vector-potential", draw_surf=False)
    #Draw(gfu)
Draw(curl(gfu), mesh, "B-field", draw_surf=False)
Draw(1 / (mu0 * mur) * curl(gfu) - mag, mesh, "H-field", draw_surf=False)


#print(SolveProblem(precond="local"))
#ps = []
#rs = []
#for p in range(1,2):
 #   r = SolveProblem(h=0.25, p=p, levels=1, condense=True,
#                     precond="bddc")
    #ps.append(p)
    #rs.append(r.copy())
    #print(r)
    #print ("p =",p,", res =",r)

#for i in range(0, len(ps)):
    #print("p =", ps[i], ", res =", rs[i])