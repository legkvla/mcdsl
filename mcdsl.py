import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
mc.postToChat("DSL initialized")

def teleport-up(up):
    playerPos = mc.player.getPos()
    mc.player.setPos(playerPos.x, playerPos.y + up, playerPos.z)
    mc.postToChat("Dont look down")
    time.sleep(1)

class Context:

    def __init__(self, playerPos):
        self.x = playerPos.x
        self.y = playerPos.y
        self.z = playerPos.z

    def left(self, val)
        self.x -= val
        self

    def right(self, val)
        self.x += val
        self

    def up(self, val)
        self.y -= val
        self

    def down(self, val)
        self.y += val
        self

    def forward(self, val)
        self.z += val
        self

    def backward(self, val)
        self.z -= val
        self

    def block(self, kind)
        mc.setBlock(x, y, z, kind)
        self
