import objgraph
x=[]
y=[x,[x],dict(x=x)]
objgraph.show_refs([y], filename='sample.png')