import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
import random

class TicTacToeApp(App):
    def on_start(self):
        self.ask_for_symbol()
    
    def build(self):
        self.player_symbol = ''  # Add this line to store the player's symbol
        layout = GridLayout(cols=3, rows=3)
        self.buttons = []
        self.player_turn = True
        self.game_over = False
        for i in range(9):
            btn = Button(text=' ', font_size=32, background_color=[1,1,1,1])
            btn.bind(on_press=self.on_button_press)
            layout.add_widget(btn)
            self.buttons.append(btn)
        self.ask_for_symbol()  # Add this line to ask the player for their symbol
        return layout


    def ask_for_symbol(self):
        # Create the symbol selection buttons
        button_x = Button(text='X', font_size=32)
        button_x.bind(on_press=self.on_symbol_x_press)
        button_o = Button(text='O', font_size=32)
        button_o.bind(on_press=self.on_symbol_o_press)
        layout = GridLayout(cols=2)
        layout.add_widget(button_x)
        layout.add_widget(button_o)

       # Create the popup
        self.popup = Popup(title='Choose Your Symbol', content=layout,
                           size_hint=(None, None), size=(200,100))

        # Show the popup
        self.popup.open()

    def on_symbol_x_press(self, button):
        self.player_symbol = 'X'
        self.popup.dismiss() 

    def on_symbol_o_press(self, button):
        self.player_symbol = 'O'
        self.popup.dismiss() 


    def on_button_press(self, button):
        self.player_turn = True
        if button.text == ' ':
            if self.player_symbol == 'X':  # Check the player's symbol
                button.text = 'X'
                button.background_color = [0,1,0,1]
            elif self.player_symbol == 'O':
                button.text = 'O'
                button.background_color = [1,1,0,1]
            self.check_game_over()
            if not self.game_over:
                self.make_computer_move()

            


    def make_computer_move(self):
        # Choose a random button to place the symbol on
        self.player_turn = False
        empty_buttons = [btn for btn in self.buttons if btn.text == ' ']
        if empty_buttons:
            btn = random.choice(empty_buttons)
            if self.player_symbol == 'X':
                btn.text = 'O'
                btn.background_color = [1,1,0,1]
            elif self.player_symbol == 'O':
                btn.text = 'X'
                btn.background_color = [0,1,0,1]

            self.check_game_over()


    def show_winner_popup(self, computer_won=False):
        # Create the congratulations message
        print("computer_won:",computer_won)
        if computer_won:
            label = Label(text='I won!', font_size=32, 
                        halign='center', valign='middle',
                        text_size=(400,100), size_hint=(None, None),
                        size=(400,100))
        else:
            label = Label(text='Congratulations!\nYou won!', font_size=32, 
                        halign='center', valign='middle',
                        text_size=(400,100), size_hint=(None, None),
                    size=(400,100))
        # Set the label's color to rainbow colors
        label.color = (1,0,0,1)
        label.bind(size=label.setter('text_size'))

        # Create the popup
        popup = Popup(title='Game Over', content=label, auto_dismiss=True,
                    size_hint=(None, None), size=(400,100))

        # Load and play the "ding ding ding" sound
        sound = SoundLoader.load('Ding-ding-ding.mp3')
        if sound:
            sound.play()

        # Show the popup
        popup.open()

    def check_game_over(self):
        # Check for a win by rows
        for i in range(3):
            if self.buttons[i].text == self.buttons[i+3].text == self.buttons[i+6].text != ' ':
                self.game_over = True
                if self.player_turn:
                    self.show_winner_popup()
                else:
                    self.show_winner_popup(computer_won=True)
                return
        
        # Check for a win by columns
        for i in range(3):
            if self.buttons[i].text == self.buttons[i+1].text == self.buttons[i+2].text != ' ':
                self.game_over = True
                if self.player_turn:
                    self.show_winner_popup()
                else:
                    self.show_winner_popup(computer_won=True)
                return
        
        # Check for a win by diagonal
        if self.buttons[0].text == self.buttons[4].text == self.buttons[8].text != ' ':
            self.game_over = True
            if self.player_turn:
                    self.show_winner_popup()
            else:
                self.show_winner_popup(computer_won=True)
            return

        if self.buttons[2].text == self.buttons[4].text == self.buttons[6].text != ' ':
            self.game_over = True
            if self.player_turn:
                    self.show_winner_popup()
            else:
                self.show_winner_popup(computer_won=True)
            return

        # Check for a win in the last row
        if self.buttons[6].text == self.buttons[7].text == self.buttons[8].text != ' ':
            self.game_over = True
            if self.player_turn:
                    self.show_winner_popup()
            else:
                self.show_winner_popup(computer_won=True)
            return

         # Check for a win in the second row
        if self.buttons[3].text == self.buttons[4].text == self.buttons[5].text != ' ':
            self.game_over = True
            if self.player_turn:
                    self.show_winner_popup()
            else:
                self.show_winner_popup(computer_won=True)
            return

if __name__ == '__main__':
    TicTacToeApp().run()
