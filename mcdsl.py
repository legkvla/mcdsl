import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
mc.postToChat("DSL initialized")

def teleport-up(height):
  playerPos = mc.player.getPos()
  mc.player.setPos(playerPos.x, playerPos.y + height, playerPos.z)
  mc.postToChat("Dont look down")
  time.sleep(1)
