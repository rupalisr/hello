from cx_Freeze import setup,Executable
setup(name="e-mail",
         version="1.0"
         author="rupali"
         description="you can send email through this programm"
         executables=[Executable(r"E:\python\validemail.py")
                        icon=r"E:\python\Email chat2.ico
                        shortcutname="sendmail"
                        shortcutDir="DesktopFolder")]
      
      ) 
                      
     
