class pyHTransform2D:
    def __init__(self,sx=1,sy=1,tx=0,ty=0):
        self.sx=sx
        self.sy=sy
        self.tx=tx
        self.ty=ty
    def transform(self,x,y):
        sx=self.sx
        sy=self.sy
        tx=self.tx
        ty=self.ty
        return x*sx+tx,y*sy+ty
    def itransform(self,x,y):
        sx=self.sx
        sy=self.sy
        tx=self.tx
        ty=self.ty
        return (x-tx)/sx,(y-ty)/sy
    def scale(self,x,y):
        return x*self.sx,y*self.sy


