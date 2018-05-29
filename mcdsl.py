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

class Context(object):

    playerPos = mc.player.getPos()

    def __init__(self):
        self.x = self.playerPos.x
        self.height = self.playerPos.y
        self.z = self.playerPos.z

    def buildx(self, x, height, kind):
        for dx in range(x):
            for dh in range(height):
                mc.setBlock(self.x + dx, self.height + dh, self.z, kind)
        self.x += x
        self.height += height

    def buildz(self, z, height, kind):
        for dz in range(z):
            for dh in range(height):
                mc.setBlock(self.x, self.height + dh, self.z + dz, kind)
        self.z += z
        self.height += height

    def build(self, x, z, height, kind):
        #self.x += x
        #self.z += z
        #self.y += height
        mc.setBlock(self.x, self.height, self.z, kind)
