from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen , ScreenManager
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
import arabic_reshaper
from bidi.algorithm import get_display
import webbrowser as wb
from kivy.uix.filechooser import FileChooserListView
import pypdf
from pypdf import PdfReader

Window.clearcolor=.4,.1,.2,.7

Window.size=350,600
Builder.load_file('ss.kv')
class StartScreen(Screen,Widget):
    bidi_text=StringProperty('')
    def __init__(self, **kwargs): 
        super(StartScreen,self).__init__(**kwargs)
        reshaped_text=arabic_reshaper.reshape(u"القرأن الكريم")
        self.bidi_text2=get_display(reshaped_text)
        
        
        reshaped_text=arabic_reshaper.reshape(u"كتاب السنة النبوية الشريفة")
        self.bidi_text3=get_display(reshaped_text)
        
        reshaped_text=arabic_reshaper.reshape(u"المسبحة الرقمية")
        self.bidi_text4=get_display(reshaped_text)
        
        reshaped_text=arabic_reshaper.reshape(u"""
        لا تنسوا الصلاة على النبى
        شكرا لكم لتحميل التطبيق 
        اعطانا الله واعطاكم الاجر والثواب                                      
        """)
        self.bidi_text5=get_display(reshaped_text)
        
        reshaped_text=arabic_reshaper.reshape(u"تمت البرمجة بواسطة محمد سمير")
        self.bidi_text6=get_display(reshaped_text)
class RootWidget(ScreenManager):
    pass
class MasbahaPage(Screen,Widget):
    bidi_text7=StringProperty('')
    bidi_text8=StringProperty('')
    bidi_text9=StringProperty('')
    bidi_text10=StringProperty('')
    
    def __init__(self, **kwargs):
        super(MasbahaPage,self).__init__(**kwargs)
        reshaped_text=arabic_reshaper.reshape(u"الرجوع للخلف")
        self.bidi_text7=get_display(reshaped_text)
        
        reshaped_text=arabic_reshaper.reshape(u"عداد المسبحة")
        self.bidi_text8=get_display(reshaped_text)
        
        reshaped_text=arabic_reshaper.reshape(u"سبح")
        self.bidi_text9=get_display(reshaped_text)
        
        reshaped_text=arabic_reshaper.reshape(u"تصفيرالرقم")
        self.bidi_text10=get_display(reshaped_text)
        
        
        
        
        
    def n_plus(self):
        value=self.ids.mylabel.text
        self.ids.mylabel.text=str(int(value)+1)
        
    def zero(self):
        value=self.ids.mylabel.text
        self.ids.mylabel.text='0'
        
    
class Quranbook(Screen,Widget):
    bidi_text11=StringProperty('')
    bidi_text12=StringProperty('')
    bidi_text13=StringProperty('')
    
    def __init__(self, **kwargs):
        super(Quranbook,self).__init__(**kwargs)
        reshaped_text=arabic_reshaper.reshape(u"رجوع للخلف")
        self.bidi_text11=get_display(reshaped_text)
        
        reshaped_text=arabic_reshaper.reshape(u"اعوذ بالله من الشيطان الرجيم")
        self.bidi_text12=get_display(reshaped_text)
        
        reshaped_text=arabic_reshaper.reshape(u"القرأن الكريم")
        self.bidi_text13=get_display(reshaped_text)
        
        
    def read(self):
        wb.open_new("file:///C:/Users/sfs/Downloads/quran/itachi/Quran.pdf")
        
    
    
    
class SonaBookScfreen(Screen,Widget):
    bidi_text14=StringProperty('')
    bidi_text15=StringProperty('')
    bidi_text16=StringProperty('')
    bidi_text17=StringProperty('')
    bidi_text18=StringProperty('')
    
    
    
    def __init__(self, **kwargs):
        super(SonaBookScfreen,self).__init__(**kwargs)
        reshaped_text=arabic_reshaper.reshape(u"رجوع للخلف")
        self.bidi_text14=get_display(reshaped_text)
        
        reshaped_text=arabic_reshaper.reshape(u"صحيح احاديث")
        self.bidi_text15=get_display(reshaped_text)
        
        reshaped_text=arabic_reshaper.reshape(u"السيرة النبوية الاولى")
        self.bidi_text16=get_display(reshaped_text)
        
        reshaped_text=arabic_reshaper.reshape(u"السيرة النبوية الثانيه")
        self.bidi_text17=get_display(reshaped_text)
        
        reshaped_text=arabic_reshaper.reshape(u"السيرة النبوية الثالثة")
        self.bidi_text18=get_display(reshaped_text)
        
        
    def read2(self):
        wb.open_new(r'file:///C:/Users/sfs/Downloads/quran/itachi/sahih_ahadis.pdf')
        
    def read3(self):
        wb.open_new(r'file:///C:/Users/sfs/Downloads/quran/itachi/syra_nabwya1.pdf')
        
    def read4(self):
        wb.open_new(r'file:///C:/Users/sfs/Downloads/quran/itachi/syra_nabwya2.pdf')
        
    def read5(self):
        wb.open_new(r'file:///C:/Users/sfs/Downloads/quran/itachi/syra_nabwya3.pdf')
        
        
        
        
class Main(App):
    def build(self):
        return RootWidget()
    
Main().run()
