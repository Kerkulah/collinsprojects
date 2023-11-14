import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.utils import get_random_color
import json

class RegistrationApp(App):
    def build(self):
        self.title = "Registration Form"
        Layout = BoxLayout(orientation='vertical', padding=30, spacing=10)

        
        head_label = Label(text='User Registration', font_size=26, bold=True, height=40)

        # adding Label
        lastName_label = Label(text='Last Name', font_size=18)
        self.lastName_input = TextInput(multiline=False, font_size=20)


        firstName_label = Label(text='First Name', font_size=18)
        self.firstName_input = TextInput(multiline=False, font_size=20)


        email_label = Label(text='Email', font_size=18)
        self.email_input = TextInput(multiline=False, font_size=20)

       

        password_label = Label(text='Password', font_size=18)
        self.password_input = TextInput(multiline=False, font_size=20, password=True)

        confirm_label = Label(text='Confirm password', font_size=18)
        self.confirm_input = TextInput(multiline=False, font_size=20, password=True)

        # Button
        submit_button = Button(text='Register', font_size=18, on_press=self.register)
        submit_button.background_color = get_random_color()
        login_button = Button(text='LogIn', font_size=18, on_press=self.show_login_popup)
        login_button.background_color = get_random_color()

        Layout.add_widget(head_label)
        Layout.add_widget(lastName_label)
        Layout.add_widget(self.lastName_input)
        Layout.add_widget(firstName_label)
        Layout.add_widget(self.firstName_input)
        Layout.add_widget(email_label)
        Layout.add_widget(self.email_input)
        Layout.add_widget(password_label)
        Layout.add_widget(self.password_input)
        Layout.add_widget(confirm_label)
        Layout.add_widget(self.confirm_input)
        Layout.add_widget(submit_button)
        Layout.add_widget(login_button)

        return Layout

    def show_login_popup(self, instance):
        login_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        userlastName_input = TextInput(multiline=False, hint_text="Email")
        password_input = TextInput(multiline=False, hint_text="Password", password=True)
        login_button = Button(text="Sign In", on_press=self.login)
        login_button.background_color = get_random_color()

        self.login_popup = Popup(
            title='Please sign in', content=login_layout, size_hint=(None, None), size=(400, 350)
        )

        login_layout.add_widget(userlastName_input)
        login_layout.add_widget(password_input)
        login_layout.add_widget(login_button)

        # Open the login popup
        self.login_popup.open()

    def login(self, instance):
        # Get the email and password entered by the user in the login popup
        popup_layout = self.login_popup.content

        if len(popup_layout.children) >= 2:
            email = popup_layout.children[0].text
            password = popup_layout.children[1].text

            try:
                # Attempt to open and read the JSON file using the email as the key
                filename = email + '.json'
                with open(filename, 'r') as file:
                    user_data = json.load(file)
                    stored_email = user_data.get('Email', '')
                    stored_password = user_data.get('Password', '')

                if email == stored_email and password == stored_password:
                    # Both email and password match, perform successful login actions
                    message2 = 'Login Successful!'
                else:
                    message2 = 'Incorrect Email or Password'
            except FileNotFoundError:
                message2 = 'User not found'
        else:
            message2 = 'Invalid login popup structure'

        # Dismiss the login popup
        self.login_popup.dismiss()

        # Display the login status in a popup
        login_status_popup = Popup(title='Login Status', content=Label(text=message2), size_hint=(None, None), size=(300, 200))
        login_status_popup.open()

    def register(self, instance):
        # collect information
        last = self.lastName_input.text
        first = self.firstName_input.text  # Fix: Access the text attribute
        email = self.email_input.text
        password = self.password_input.text
        confirm = self.confirm_input.text

        # Validation
        if last.strip() == '' or first.strip() == '' or email.strip() == '' or password.strip() == '':
            message1 = 'Please fill in all fields'
        elif password != confirm:
            message1 = 'Password do not match'
        else:
            filename = email + '.json'
            user_data = {
                "First Name": first,
                "Last Name": last,
                "Email": email,
                "Password": password
            }
            with open(filename, 'w') as file:
                json.dump(user_data, file)

            message1 = 'Registration Successful!!\nName: {}\nEmail: {}'.format(last, email)

        # pop up
        popup = Popup(title='Registration Status', content=Label(text=message1), size_hint=(None, None), size=(400, 200))
        popup.open()


if __name__ == '__main__':
    RegistrationApp().run()
    
   

    

