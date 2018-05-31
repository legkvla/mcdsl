import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
mc.postToChat("DSL initialized")

def teleport_up(up):
    playerPos = mc.player.getPos()
    mc.player.setPos(playerPos.x, playerPos.y + up, playerPos.z)
    mc.postToChat("Dont look down")
    time.sleep(1)

def getPos():
    mc.player.getPos()

def setBlock(x, h, z, kind):
    mc.setBlock(x, h, z, kind)
    print("setBlock(" + x + ", " + h + ", " + z + " ," + kind + ")")

class Context(object):

    playerPos = getPos()

    def __init__(self):
        self.x = self.playerPos.x
        self.h = self.playerPos.y
        self.z = self.playerPos.z

    def buildh(self, dx, dz, h, kind):
        for dh in range(h):
            setBlock(self.x + dx, self.h + dh, self.z + dz, kind)

    def buildx(self, x, h, kind):
        for dx in range(x):
            self.buildh(dx, 0, h, kind)
        self.x += x

    def buildz(self, z, h, kind):
        for dz in range(z):
            self.buildh(0, dz, h, kind)
        self.z += z

    def build(self, x, z, h, kind):
        for dx in range(x):
            for dz in range(z):
                self.buildh(dx, dz, h, kind)
        self.x += x
        self.z += z

    def move(dx, dh, dz):
        self.x += dx
        self.z += dz
        self.h += dh
