from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Recipe

# Create your views here.

def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_price = data.get('recipe_price')
        recipe_image = request.FILES.get('recipe_image')

        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_price=recipe_price,
            recipe_image=recipe_image,
        )
        return redirect('/recipes/')
    
    queryset = Recipe.objects.all()
    context = {'recipes':queryset}

    return render(request, 'recipe.html', context)

## delete recipes
# def recipedelete(request, pk):
#     recipe = Recipe.objects.get(id=pk)
#     recipe.delete()
#     return redirect('recipes')

def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    context = {'recipes':queryset}  
    return render(request, 'update_recipe.html', context)



def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')

def recipeHome(request):
        return render(request, 'recipeHome.html')


