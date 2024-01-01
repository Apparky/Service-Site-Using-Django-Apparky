from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.


def home(request):
    return HttpResponse('This is My Service Pge')


def index(request):
    product_filter_dict = {
        'Web_Development': 'Web Development',
        'Desktop_Applications': 'Desktop Applications',
        'Mobile_Applications': 'Mobile Applications',
        'Next_JS_SEO': 'Next JS SEO'
    }
    """
    for product in product_filter_dict:
        print(f'{product} : {product_filter_dict[product]}')
    """
    portfolios = Portfolio.objects.filter(Portfolio_Display_Status=True)
    return render(request, 'index.html', {'portfolios': portfolios, 'products': product_filter_dict})


def portfolio_details(request, p_slug):
    portfolios = Portfolio.objects.filter(portfolio_slug=p_slug)
    return render(request, 'portfolio-details.html', {'portfolios': portfolios})


def contact_us(request):
    contact_header_info = Contact_Header_and_Info_dumy.objects.filter(status=1)
    if request.method == "POST":
        contact = Contact_Us_Form()

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact.contact_name = name
        contact.contact_email = email
        contact.contact_subject = subject
        contact.contact_message = message
        contact.contact_status = False

        contact.save()
        return render(request, 'contact-sent.html', {'header_info': contact_header_info})

    return render(request, 'contact.html', {'header_info': contact_header_info})


def services(request):
    service_header = Our_service_Header.objects.filter(status=1)
    serv_header = ""
    for serv in service_header:
        serv_header += f'{serv.Header}. '

    all_services = Our_Service.objects.all()

    our_happy_client_header = Our_Client_Header.objects.all()
    happy_client = ""
    for client in our_happy_client_header:
        happy_client += f'{client.Header}. '

    client_images = Our_Client.objects.filter(priority_status=1)

    testimonial_header = Testimonials_Header.objects.filter(status=1)
    test_header = ""
    for header in testimonial_header:
        test_header += f'{header.Header}. '

    testimonials = Testimonials.objects.filter(status=1)

    return render(request, 'service.html',
                  {'serv_header': serv_header, 'service': all_services, 'happy_client': happy_client,
                   'clients': client_images, 'test_header': test_header,
                   'testimonials': testimonials})


def about(request):
    our_team_header = Our_Team_Heading.objects.filter(status=1)
    header = ""
    for Header in our_team_header:
        header += f'{Header.Heading}. '

    team_member = Our_Team.objects.all()
    return render(request, 'about.html', {'team_header': header, 'members': team_member})


def pricing(request):
    return render(request, 'pricing.html')


def faq(request):
    faq_header = Faq_Header.objects.filter(status=1)
    header = ""
    for faq_ in faq_header:
        header += f'{faq_.Header}. '

    faqs = Faq_Sets.objects.filter(status=1)
    total_faqs = []
    for i in range(1, (len(faqs) + 1)):
        total_faqs.append(i)

    """print(total_faqs)"""
    return render(request, 'faq.html', {'header': header, 'faqs': faqs, 'total': total_faqs})


def blog(request):
    blog_header = Blog_header.objects.filter(Blog_Display_Status=True)
    header = ""
    for blog_ in blog_header:
        header += f'{blog_.Blog_header_for_blog_page}'

    blog_content = Blog_Content.objects.filter(Blog_Display_Status=True)

    return render(request, 'blog.html', {'header': header, 'blogs': blog_content})


def blog_details(request, b_slug):
    blogs = Blog_Content.objects.filter(Blog_Slug=b_slug)
    return render(request, 'blog-details.html')



