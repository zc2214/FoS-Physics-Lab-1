import math
heighttol=13.280
diameter=4.865
heightup=0.50
heightdown=0.25
height=heighttol-heightup-heightdown
print (height)
pi=3.14
volume=pi*((diameter/2)**2)*height
print (volume)
uncertaintyheighttol=0.003
uncertaintyheightup=0.05
uncertaintyheightdown=0.05
uncertaintyheight=(uncertaintyheighttol**2+uncertaintyheightup**2+uncertaintyheightdown**2)**0.5
print(uncertaintyheight)
uncertaintydiameter=0.003
uncertaintyvolume=(uncertaintyheight/height+2*(uncertaintydiameter/diameter))*volume
print(uncertaintyvolume)
actualvolume=245
percentageerror=(actualvolume-volume)/actualvolume
print(percentageerror)

