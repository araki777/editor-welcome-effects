import random

from terminaltexteffects.effects import (
  effect_beams,
  effect_binarypath,
  effect_blackhole,
  effect_bouncyballs,
  effect_bubbles,
  effect_burn,
  effect_colorshift,
  effect_crumble,
  effect_decrypt,
  effect_errorcorrect,
  effect_expand,
  effect_fireworks,
  effect_highlight,
  effect_laseretch,
  effect_matrix,
  effect_middleout,
  effect_orbittingvolley,
  effect_overflow,
  effect_pour,
  effect_print,
  effect_rain,
  effect_random_sequence,
  effect_rings,
  effect_scattered,
  effect_slice,
  effect_slide,
  effect_spotlights,
  effect_spray,
  effect_swarm,
  effect_sweep,
  effect_synthgrid,
  effect_unstable,
  effect_vhstape,
  effect_waves,
  effect_wipe,
)

# テキストファイルを開いて行をリストに格納
with open("AA.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

text_data = "".join(lines)

effects = [
  lambda text: effect_beams.Beams(text),
  lambda text: effect_binarypath.BinaryPath(text),
  lambda text: effect_blackhole.BlackHole(text),
  lambda text: effect_bouncyballs.BouncyBalls(text),
  lambda text: effect_bubbles.Bubbles(text),
  lambda text: effect_burn.Burn(text),
  lambda text: effect_colorshift.ColorShift(text),
  lambda text: effect_crumble.Crumble(text),
  lambda text: effect_decrypt.Decrypt(text),
  lambda text: effect_errorcorrect.ErrorCorrect(text),
  lambda text: effect_expand.Expand(text),
  lambda text: effect_fireworks.Fireworks(text),
  lambda text: effect_highlight.Highlight(text),
  lambda text: effect_laseretch.Laseretch(text),
  lambda text: effect_matrix.Matrix(text),
  lambda text: effect_middleout.MiddleOut(text),
  lambda text: effect_orbittingvolley.OrbittingVolley(text),
  lambda text: effect_overflow.Overflow(text),
  lambda text: effect_pour.Pour(text),
  lambda text: effect_print.Print(text),
  lambda text: effect_rain.Rain(text),
  lambda text: effect_random_sequence.RandomSequence(text),
  lambda text: effect_rings.Rings(text),
  lambda text: effect_scattered.Scattered(text),
  lambda text: effect_slice.Slice(text),
  lambda text: effect_slide.Slide(text),
  lambda text: effect_spotlights.Spotlights(text),
  lambda text: effect_spray.Spray(text),
  lambda text: effect_swarm.Swarm(text),
  lambda text: effect_sweep.Sweep(text),
  lambda text: effect_synthgrid.SynthGrid(text),
  lambda text: effect_unstable.Unstable(text),
  lambda text: effect_vhstape.VhsTape(text),
  lambda text: effect_waves.Waves(text),
  lambda text: effect_wipe.Wipe(text),
]

effect = random.choice(effects)(text_data)

with effect.terminal_output() as terminal:
    for frame in effect:
        terminal.print(frame)
