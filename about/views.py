from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'ABOUT',
        'subjudul':'Tentang website belajar asik',
        'banner':'img/banner_about.png',
        'app_css': 'about/css/styles.css',
        'nav' : [
            ['/' , 'Home'],
            ['/blog' , 'Blog'],
            ['/about' , 'About'],
            ['/contact', 'Contact']
        ]
    }
    return render(request,'about/index.html', context)