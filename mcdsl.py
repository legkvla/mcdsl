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

    def right(self, val):
        self.x -= val
        self

    def left(self, val):
        self.x += val
        self

    def down(self, val):
        self.y -= val
        self

    def up(self, val):
        self.y += val
        self

    def forward(self, val):
        self.z += val
        self

    def backward(self, val):
        self.z -= val
        self

    def block(self, kind):
        mc.setBlock(self.x, self.y, self.z, kind)
        self
