from django.shortcuts import render
from .models import Department, TeamMember
# Create your views here.
def home(request):
    return render(request, 'home.html')

def home(request):
    leader = TeamMember.objects.filter(is_leader=True).first()
    departments = Department.objects.all()

    return render(request, 'home.html', {
        'leader': leader,
        'departments': departments
    })

def join(request):
    return render(request, 'join.html')
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def field_detail(request, name):
    data = {
        "programming": "بناء مواقع وتطبيقات والعاب باحترافيه بواسطه لغات مثل python _ html_ css_ JavaScript",
        "marketing": "التسويق هو الترويج للمنتجات بواسطه التسويق الرقمي او اداره السوشيال ميديا او الاعلانات ",
        "design": "الجرافيك ديزاين هو فن التصميم علي مواقع زي Photoshop و Illustrator وتصميم Logos وتصميم اعلانات",
        "business": "ريادة الأعمال هي إنشاء مشاريع وادارتها والتسويق والتخطيط المادي والتفكير الابداعي ",
        "security": "الأمن السيبراني هو حماية الأنظمة وحمايه البيانات واختبار الاختراق وبتتعلم Ethical Hacking_ Network Security",
        "content": "صناعة المحتوى هي إنشاء فيديوهات أو مقالات وكتابه محتوي ومونتاج وتصوير وبناء جمهور "
    }

    context = {
        "title": name,
        "description": data.get(name, "مفيش معلومات حالياً")
    }

    return render(request, 'field.html', context)