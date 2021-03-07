"""
https://itchallengeforfuture.postfinance.ch/en/?utm_source=fbkplatform&utm_medium=paidsocial&utm_campaign=KOM00041%28a_postfinance%29%28y_2021%29%28q_1%29%28m_mar%29%28p_EVP_IT%29%28g_consideration%29%28o_traffic%29%28n_FBK-INS%29%28t_RTG_Video50%25%29%28l_EN%29&utm_content=6234232599344%E2%80%8B&fbclid=IwAR2xe6KF7uRZUpq0Y-7GWniEJFPtLFKgg7txoJkXegQhkMwZFLxl5OonCZc
"""
class Graph(object):
    def __init__(self,vertices):
        self.vertices = vertices
            
    def allDistances(self):
        for v in self.vertices[0:6]:
            for i in v.connections[::-1]:
                w = self.vertices[i]
                d = self.distance(v,w)
                print("[{}-{}]={}".format(v.name,w.name,d))

    def printCost(self,queue):
        for q in queue:
            print("{}->{}".format(q[0].name,q[1]))
        print("")
    
    def distance(self,v1,v2):
        x = pow(v2.x-v1.x,2)
        y = pow(v2.y-v1.y,2)
        return pow(x+y,1/2)
    
    def uniformCost(self,v):
        queue = list() 
        for i in v.connections:
            d = self.distance(v,self.vertices[i])
            queue.append((self.vertices[i],d))
        while queue:
            #self.printCost(queue)
            x = queue.pop()
            if x[0].name == "S":
                return x
            else:
                queue.extend([(self.vertices[i],x[1]+self.distance(x[0],self.vertices[i])) for i in x[0].connections])
                queue.sort(key=byCost,reverse=True)
        return None

    def solve(self):
        q = self.uniformCost(self.vertices[0])
        print("distance: {}\n".format(q[1]))
        return q[1]

class Vertex(object):
    def __init__(self,x,y,connections,name):
        self.x=x
        self.y=y
        self.connections = connections
        self.marked=False     
        self.name=name 

def byCost(e):
    return e[1]

if __name__=='__main__':
    #POSTFINANCE HQ
    v0=Vertex(3,5,[1,2],"S")
    #POWERCODER-activities
    v11=Vertex(10,8,[3],"1")
    v12=Vertex(11,3,[4,5],"2")
    v13=Vertex(14,7,[1,5],"3")
    v14=Vertex(15,1,[2,6],"4")
    v15=Vertex(18,5,[2,3,6],"5")
    #POWERCODER  
    v1=Vertex(22,2,[1,3],"S")
    #EDUCREATORS-activities
    v21=Vertex(26,4,[2],"1")
    v22=Vertex(35,8,[1,3,4],"2")
    v23=Vertex(26,9,[2,4,5],"3")
    v24=Vertex(28,13,[2,3,6],"4")
    v25=Vertex(19,9,[3,6],"5")
    #EDUCREATORS
    v2=Vertex(19,13,[1],"S")
    #DSD_FUNDATION-activities
    v31=Vertex(21,15,[2],"1")
    v32=Vertex(24,17,[3,4],"2")
    v33=Vertex(30,15,[2,6],"3")
    v34=Vertex(34,17,[2,5],"4")
    v35=Vertex(46,15,[4,6],"5")
    #DSD_FUNDATION
    v3=Vertex(38,14,[1],"S")
    #CHARITYEVENT-activities
    v41=Vertex(42,13,[2,5],"1")
    v42=Vertex(41,2,[1,3,4],"2")
    v43=Vertex(46,9,[2,6],"3")
    v44=Vertex(48,3,[2,6],"4")
    v45=Vertex(51,14,[1,6],"5")
    #CHARITYEVENT
    v4=Vertex(54,8,[],"S")

    #GRAPHS
    G1 = Graph([v0,v11,v12,v13,v14,v15,v1])
    G2 = Graph([v1,v21,v22,v23,v24,v25,v2])
    G3 = Graph([v2,v31,v32,v33,v34,v35,v3])
    G4 = Graph([v3,v41,v42,v43,v44,v45,v4])
    graphs = [G1,G2,G3,G4]

    distance=0
    for g in graphs:
        distance+=g.solve()

    print("----------")
    print("distance: ~{:.2f}".format(distance))
    print("----------")