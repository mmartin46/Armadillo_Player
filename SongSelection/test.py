# Mitchell Martin
# 12/21/2022
# Song Selection

class SongScreen(Screen):
   def __init__(self, **kw):
      super().__init__(**kw)
      
   def on_enter(self, *args):
      # BackDrop Layout
      self.back_drop = MDFloatLayout()

      # Title Layout
      self.title_lout = MDFloatLayout()
      self.title_lout.size_hint_y=.11
      self.title_lout.pos_hint={"center_y": .95}
      self.title_lout.md_bg_color=[ 72/255, 31/255, 255/255, 1 ]
      
      # Label for Title Layout
      self.title_label=MDLabel()
      self.title_label.text='Hebrews'
      self.title_label.font_style="H1"
      self.title_label.pos_hint={"center_y": .5}
      self.title_label.halign="center"
      self.title_label.font_size="25sp"
      self.title_label.theme_text_color="Custom"
      self.title_label.text_color=[ 240/255, 240/255, 240/255, 1 ]
      self.title_lout.add_widget(self.title_label)