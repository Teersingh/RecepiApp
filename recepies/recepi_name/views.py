from django.shortcuts import render
from .models import recepies
from django.http import HttpResponse

# Create your views here.
def index(request):
    try:
        if request.method == 'POST':
            data=request.POST
            # print(data)

            recipe_name=data.get('recepi_n')
            description=data.get('description')
            image=request.FILES.get('image')
            print(recipe_name)
            print(description)
            print(image)


            recepies.objects.create(
            recepi_n=recipe_name,
            description=description,
                image=image
            )

            return render(request,'base.html')
        else:
            return render(request, 'base.html') 
    
    except Exception as e:
        return HttpResponse("An error occurred: " + str(e))
 
def home(request):
  data=recepies.objects.all()

  l=[]
  for char in data:
    l.append(char.recepi_n)
  print(l)
#   print(name)
#   f_data=recepies.objects.filter(recepi_n=name).first()
#   print(f_data.recepi_n)
#   print(f_data.description)
#   print(f_data.image)

  

  return render(request,'home.html',context={"names": l})


def recepi(request,name):
#    print(name)
   f_data=recepies.objects.filter(recepi_n=name).first()
   

   return render(request,'index.html', context={'f_data':f_data})