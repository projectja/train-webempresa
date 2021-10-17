from .models import Page

def ctx_dict_pages(request):
    ctx_pages = {}
    pages =  Page.objects.all()
    for page in pages:
        ctx_pages[page.title] = page.title
        print(ctx_pages)
    return ctx_pages
        

