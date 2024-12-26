import vpype as vp
import vsketch


class BorderSketch(vsketch.SketchClass):
    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size('a0', landscape=False, center=False)
        vsk.scale('mm')

        width = 700
        height = 1100
        sm_mark_len = 2.5
        bg_mark_len = 5

        vsk.line(0,0, width, 0)
        vsk.line(0,0, 0, height)
        for x in range(1, width // 10 +1):
            if x % 10 != 0:
                vsk.line(x*10,0, x*10,sm_mark_len)
            else:
                vsk.line(x*10,0, x*10,bg_mark_len)
        for y in range(1, height // 10 +1):
            if y % 10 != 0:
                vsk.line(0,y*10, sm_mark_len,y*10)
            else:
                vsk.line(0,y*10, bg_mark_len,y*10)
        vsk.save("border_a0.svg")

if __name__ == "__main__":
    BorderSketch.display()
