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
        self.y = self.playerPos.y
        self.z = self.playerPos.z

    def buildx(self, x, height, kind):
        #self.x += x
        #self.y += height
        mc.setBlock(self.x, self.y, self.z, kind)

    def buildz(self, z, height, kind):
        #self.z += z
        #self.y += height
        mc.setBlock(self.x, self.y, self.z, kind)

    def build(self, x, z, height, kind):
        #self.x += x
        #self.z += z
        #self.y += height
        mc.setBlock(self.x, self.y, self.z, kind)
