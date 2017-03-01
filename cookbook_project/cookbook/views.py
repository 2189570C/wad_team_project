# DJANGO IMPORTS
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# COOKBOOK IMPORTS
from cookbook.models import Category, Recipe, Comment, Ingredient
from cookbook.forms import UserForm, IngredientForm, RecipeForm

#-HOME-SECTION----------------------------------------------------------

def home(request):
    context_dict = {}
    best_rated = Recipe.objects.order_by('-rating')[:5]
    new_recipes = Recipe.objects.order_by('-upload_date')[:5]
    context_dict['best_rated'] = best_rated
    context_dict['new_recipes'] = new_recipes
    #when template is made
    response = render(request, 'cookbook/home.html', context_dict)
    #response = HttpResponse("This is the home")
    return response

#-USER-SECTION----------------------------------------------------------

def signup(request):
    registered = False

    if request.method == 'POST':
        # check if form is valid
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            # create user
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True

        else:
            # invalid form/errors, print to terminal
            print(user_form.errors)

    else:
        # create blank form
        user_form = UserForm()

    context_dict = {}
    context_dict['user_form'] = user_form
    context_dict['registered'] = registered
    
    return render(request, 'cookbook/signup.html', context_dict)

def user_login(request):
    context_dict = {}

    if request.method == 'POST':
        # check if username and password are valid
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            # check account is not disabled
            if user.is_active:
                # login the user
                login(request, user)
                return HttpResponseRedirect(reverse('myprofile'))
            else:
                # inactive account
                context_dict['errors'] = ['Your CookBook account is disabled.']
                #return render(request, LOGIN HTML, context_dict)
                return HttpResponse('disabled account')
        else:
            # invalid login details
            print('Invalid login details: {0}, {1}'.format(username, password))
            context_dict['errors'] = ['Invalid login details']
            #return render(request, LOGIN HTML, context_dict)
            return HttpResponse('Invalid login details')
        
    else:
        # Not HTTP POST
        #return render(request, LOGIN HTML, context_dict)
        return HttpResponse('login here')

@login_required
def user_logout(request):
    # logout user and redirect to home page
    logout(request)
    return HttpResponRedirect(reverse('home'))

@login_required
def myprofile(request):
    context_dict = {}
    
    recent_comments = Comment.objects.filter(user=request.user)
    if recent_comments:
        recent_comments = recent_comments.order_by(['-upload_date'])[:10]
        
    recipes = Recipe.objects.filter(user=request.user)
    if recipes:
        recipe = recipes.order_by(['-upload_date'])

    context_dict['recent_comments'] = recent_comments
    context_dict['recipes'] = recipes

    return render(request, 'cookbook/myprofile.html', context_dict)

@login_required
def savedrecipes(request):
    context_dict = {}

    saved_recipes = Recipe.objects.filter(saved_by=request.user)
    context_dict['saved_recipes'] = saved_recipes
    
    return HttpResponse("saved recipes")

@login_required
def uploadrecipe(request):
    context_dict = {}
    
    if request.method == 'POST':
        # check if form is valid
        recipe_form = RecipeForm(request.POST)
        
        if form.is_valid():
            # create
            recipe = recipe_form.save(commit=False)
            recipe.user = request.user

            if recipe.is_vegan or (recipe.is_vegetarian and recipe.is_dairy_free):
                recipe.is_vegan = True
                recipe.is_vegetarian = True
                recipe.is_dairy_free = True

            recipe.save()
            return view_recipe(request, request.user.username, recipe.name)

        else:
            print(form.errors)

    context_dict['form'] = RecipeForm()
    #return render(request, UPLOAD HTML, context_dict)    
    return HttpResponse("upload recipe")

# view for a user profile
def view_user(request, user):
    context_dict = {}

    try:
        user = User.objects.get(username=user)
        if user == request.user:
            return HttpResponseRedirect(reverse('myprofile'))
            
        recipes = Recipe.objects.filter(user=user)

        context_dict['author'] = user
        context_dict['recipes'] = recipes

    except User.DoesNotExist:
        context_dict['author'] = None
        context_dict['recipes'] = None
    
    return HttpResponse("view someone elses profile")

# Actual recipe view
def view_recipe(request, user, recipe_slug):
    context_dict = {}

    if request.method == 'GET':

        try:
            # get the recipe
            user = User.objects.get(username=user)
            recipe = Recipe.objects.get(user=user, slug=recipe_slug)
            recipe.views += 1

            # get the recipes ingredients
            ingredients = Ingredient.objects.filter(recipe=recipe)

            # get the recipes comments
            comments = Comment.objects.filter(recipe=recipe).order_by('-upload_date')

            context_dict['author'] = user
            context_dict['recipe'] = recipe
            context_dict['ingredients'] = ingredients
            context_dict['comments'] = comments


        except (User.DoesNotExist, Recipe.DoesNotExist):
            context_dict['author'] = None
            context_dict['recipe'] = None
            context_dict['ingredients'] = None
            context_dict['comments'] = None

             
        return HttpResponse("view a recipe")

    else:
        # HTTP POST (posting a comment/rating)
        return HttpResponse("comment/rating posted")


#-CATEGORY-SECTION--(finding-recipes)--------------------------------------

def categories(request):
    context_dict = {}
    categories = Category.objects.all()
    context_dict['categories'] = categories
    
    return render(request, 'cookbook/categories.html', context_dict)

# for all categories
def view_category(request, category_name):
    context_dict = {}
    try:
        category = Category.objects.get(name=category_name)
        recipes = Recipe.objects.filter(category=category)
        context_dict['category'] = category
        context_dict['recipes'] = recipes

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['recipes'] = None
    
    return HttpResponse("specific category")

def bestrated(request):
    context_dict = {}
    recipes = Recipe.objects.all().order_by('-rating')
    context_dict['recipes'] = recipes
    return HttpResponse("best rated recipes here")

# search and search results
def search(request):
    return render(request, 'cookbook/search.html')

#-HELP-SECTION------------------------------------------------------------

def about(request):
    return render(request, 'cookbook/help.html')

def faq(request):
    return HttpResponse("FAQ page")

def conversioncharts(request):
    return HttpResponse("helpful conversion charts")

def recipeguide(request):
    return HttpResponse("how to write a recipe")

def commentingrules(request):
    return HttpResponse("commenting and website rules")
