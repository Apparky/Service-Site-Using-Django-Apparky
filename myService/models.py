from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Our_Team_Heading(models.Model):
    Heading = models.TextField(null=False, blank=False, default='Put Our Heading Over Here')
    status = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return f'{self.Heading} --- {self.status}'


class Our_Team(models.Model):
    role = (
        ('Director', 'Director'),
        ('CEO', 'CEO'),
        ('Content Writer', 'Content Writer'),
        ('Founder', 'Founder'),
        ('Co Founder', 'Co Founder'),
        ('Marketing', 'Marketing'),
        ('Developer', 'Developer'),
        ('Designer', 'Designer'),
        ('Manager', 'Manager'),
        (None, None)
    )
    name = models.CharField(max_length=100, null=False, blank=False, default='Team Member Name')
    contact_no = models.CharField(max_length=20, null=False, blank=False, default=000)
    alt_contact_no = models.CharField(max_length=20, null=True, blank=True, default=000)
    eMail = models.EmailField(null=False, blank=False, default='your@email.com')
    designation = models.CharField(max_length=100, null=False, blank=False, default='Team Designation')
    role_description = models.TextField(null=False, blank=False, default='Describe the Designation')
    image = models.ImageField(null=False, blank=False, upload_to='media/images/')
    address = models.TextField(null=True, blank=True, default='Members Address')
    website = models.CharField(max_length=150, null=True, blank=True, default='www.website.com')
    twitter = models.CharField(max_length=150, null=True, blank=True, default='twitter.com/user')
    facebook = models.CharField(max_length=100, null=True, blank=True, default='facebook.com/username')
    linkdin = models.CharField(max_length=150, null=True, blank=True, default='linkdin.com/username')
    instagram = models.CharField(max_length=150, null=True, blank=True, default='inatagram.com/username')

    def __str__(self):
        return f'{self.name} --- {self.eMail} --- {self.contact_no}'


class Contact_Header_and_Info(models.Model):
    Header = models.TextField(null=True, blank=True, default=None, help_text='Put Contact Header Here')
    location = models.CharField(max_length=20, null=True, blank=True, default=None, help_text='Put Location Here')
    email = models.EmailField(null=True, blank=True, default=None, help_text='Enter Your email as "your@email.com"')
    contact = models.CharField(max_length=100, null=True, blank=True, default=None, help_text='Enter your Contact No.')
    opening_hour = models.CharField(max_length=200, null=True, blank=True, default=None, help_text='Ex. Mon-Sat 10.00 AM - 09:00 PM')
    status = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return f'{self.Header} -- {self.status}'


class Contact_Us_Form(models.Model):
    contact_name = models.CharField(max_length=100, null=False, blank=False, default='Your Name')
    contact_email = models.EmailField(null=False, blank=False, default='your@email.com')
    contact_subject = models.CharField(max_length=100, null=False, blank=False, default='Subject')
    contact_message = models.TextField(null=False, blank=False, default='Your Message')
    contact_status = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return f'{self.contact_name} --- {self.contact_status}'


class Faq_Header(models.Model):
    Header = models.TextField(null=True, blank=True, default='Put FAQ Header Here')
    status = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return f'{self.Header} --- {self.status}'


class Faq_Sets(models.Model):
    FAQ_Question = models.CharField(max_length=150, null=True, blank=True, default='Put FAQ Question over here')
    FAQ_Answer = models.TextField(null=True, blank=True, default='Put FAQ Answer over here')
    status = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return f'{self.FAQ_Question} --- {self.status}'


class Our_service_Header(models.Model):
    Header = models.TextField(null=True, blank=True, default='Put Service Header Here')
    status = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return f'{self.Header} --- {self.status}'


class Our_Service(models.Model):
    service_name = models.CharField(max_length=200, null=True, blank=True, default='Service Name')
    service_description_summary = models.TextField(null=True, blank=True, default='Service Description')
    image = models.ImageField(null=True, blank=True, upload_to='media/images/')

    def __str__(self):
        return self.service_name


class Testimonials_Header(models.Model):
    Header = models.TextField(null=False, blank=False, default='Put Testimonials Header Here')
    status = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return f'{self.Header} --- {self.status}'


class Testimonials(models.Model):
    review_set = (
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Normal', 'Normal'),
        ('Bad', 'Bad'),
        ('Worst', 'Worst'),
        (None, None)
    )
    name = models.CharField(max_length=200, null=False, blank=False, default='Name')
    contact = models.CharField(max_length=20, null=False, blank=False, default=000)
    designation = models.CharField(max_length=50, null=False, blank=False, default='Reviewer Designation')
    review = models.CharField(max_length=50, choices=review_set, null=False, blank=False, default=None)
    testimonials = models.TextField(null=False, blank=False, default='The Testimonials')
    image = models.ImageField(null=False, blank=True, upload_to='media/images/',
                              help_text='***You can only add one Picture')
    status = models.BooleanField(null=False, blank=False, default=False,
                                 help_text='***Check the Button to make it display on Your Site')

    def __str__(self):
        return f'{self.name} ---- {self.review} ---- {self.status}'


class Our_Client_Header(models.Model):
    Header = models.TextField(null=False, blank=False, default='Put Your Client Header Here')
    status = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return f'{self.Header} --- {self.status}'


class Our_Client(models.Model):
    cl_type = (
        ('Organization', 'Organization'),
        ('Person', 'Person'),
        (None, None)
    )
    client_name = models.CharField(max_length=200, null=True, blank=True, default='Client Name')
    client_contact = models.CharField(max_length=20, null=True, blank=True, default=000)
    client_alt_contact = models.CharField(max_length=20, null=True, blank=True, default=000)
    client_type = models.CharField(max_length=50, choices=cl_type, null=True, blank=True, default=None)

    owner_name = models.CharField(max_length=100, null=True, blank=True, default='Owner Name', help_text='**Fill up these Entryes only if the client is an Organization')
    owner_address = models.CharField(max_length=100, null=True, blank=True, default='Owner Address', help_text='**Fill up these Entryes only if the client is an Organization')
    owner_contact = models.CharField(max_length=20, null=True, blank=True, default=0000, help_text='**Fill up these Entryes only if the client is an Organization')
    owner_alt_contact = models.CharField(max_length=20, null=True, blank=True, default=0000, help_text='**Fill up these Entryes only if the client is an Organization')
    owner_email = models.EmailField(max_length=100, null=True, blank=True, default='owner@email.com', help_text='**Fill up these Entryes only if the client is an Organization')

    client_email = models.EmailField(max_length=100, null=True, blank=True, default='client@email.com')
    client_address = models.CharField(max_length=100, null=True, blank=True, default='Client Address')

    client_image = models.ImageField(null=True, blank=True, upload_to='media/images/', default='**You can only add one Image')

    priority_status = models.BooleanField(null=False, blank=False, default=False, help_text='**Check this box if you concider this Client Priority is High')

    def __str__(self):
        if self.client_type == 'Person':
            return f'{self.client_name} -- {self.client_contact}'
        else:
            return f'{self.client_name} --- {self.owner_name} --- {self.client_contact}'


class Portfolio(models.Model):
    p_type = (
        ('Web_Development', 'Web_Development'),
        ('Desktop_Applications', 'Desktop_Applications'),
        ('Mobile_Applications', 'Mobile_Applications'),
        ('Next_JS_SEO', 'Next_JS_SEO'),
        (None, None)
    )
    Portfolio_name = models.CharField(max_length=100, null=True, blank=True, default='Portfolio Name')
    Portfolio_type = models.CharField(max_length=100, choices=p_type, null=True, blank=True, default=None)
    Portfolio_summary = models.CharField(max_length=300, null=True, blank=True, default='Portfolio Summary')
    Portfolio_Description = models.TextField(null=True, blank=True, default='Portfolio Description')
    portfolio_slug = models.SlugField(max_length=100, null=True, blank=True, default='portfolio_slug', help_text='**Slug has to be Unique for each Portfolio')

    portfolio_image_1 = models.ImageField(null=True, blank=True, upload_to='media/images/', help_text='**You can only add one Picture')
    portfolio_image_alt_1 = models.CharField(max_length=150, null=True, blank=True, default='Image Alt', help_text='**Add ALT Tag line over here')

    portfolio_image_2 = models.ImageField(null=True, blank=True, upload_to='media/images/', help_text='**You can only add one Picture')
    portfolio_image_alt_2 = models.CharField(max_length=150, null=True, blank=True, default='Image Alt', help_text='**Add ALT Tag line over here')

    portfolio_image_3 = models.ImageField(null=True, blank=True, upload_to='media/images/', help_text='**You can only add one Picture')
    portfolio_image_alt_3 = models.CharField(max_length=150, null=True, blank=True, default='Image Alt', help_text='**Add ALT Tag line over here')

    portfolio_image_4 = models.ImageField(null=True, blank=True, upload_to='media/images/', help_text='**You can only add one Picture')
    portfolio_image_alt_4 = models.CharField(max_length=150, null=True, blank=True, default='Image Alt', help_text='**Add ALT Tag line over here')

    portfolio_publish_date = models.DateField(null=True, blank=True, default=timezone.now, help_text='**Set Published Date Here')
    portfolio_site = models.CharField(max_length=30, null=True, blank=True, default='Put Site name to display')
    portfolio_url = models.CharField(max_length=100, null=True, blank=True, default='Portfolio Url', help_text='**Put Portfolio URL here if Exists')
    Portfolio_Display_Status = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        if self.Portfolio_Display_Status is True:
            return f'{self.Portfolio_name} ---- {self.Portfolio_type} ---- Display Status is Active'

        else:
            return f'{self.Portfolio_name} ---- {self.Portfolio_type} ---- Display Status is Not Active'


class Blog_header(models.Model):
    Blog_header_for_recent_blog = models.TextField(null=True, blank=True, default='Header for Recent Blog Section', help_text='***** This Section Details Will Display on Recent Blog Section *****')
    Blog_header_for_blog_page = models.TextField(null=True, blank=True, default='Header for Blog Page Section', help_text='***** This Section Details Will Display on Blog Section *****')
    Blog_Display_Status = models.BooleanField(null=False, blank=False, default=False, help_text='***** Check This box If you wanna Display this on your Web *****')

    def __str__(self):
        return f'{self.Blog_header_for_recent_blog}  ----//---- {self.Blog_header_for_blog_page} ----//---- {self.Blog_Display_Status}'


class Blog_Content(models.Model):
    Blog_Title = models.CharField(max_length=100, unique=True, null=True, blank=True, default='Blog Title', help_text='***** Add Blog Title Over Here *****')
    Blog_Summary = models.TextField(null=True, blank=True, default='Blog Summary', help_text='***** Add Blog Summary Over Here ***** ')
    Blog_Image = models.ImageField(null=True, blank=True, upload_to='media/images/', help_text='***** Set Blog Image Over Here *****')
    Blog_ALT_TAG = models.CharField(max_length=100, null=True, blank=True, default='Blog ALT TAG', help_text='***** Put ALT TAG for SEO perpouses *****')
    Blog_Slug = models.CharField(max_length=100, unique=True, null=True, blank=True, default='Blog-Slug', help_text='***** Put Blog Title and Replace it by ( - ) is Recomended *****')

    Blog_Author_Name = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, help_text='***** Add Auther User Name *****')
    Author_Image = models.ImageField(null=True, blank=True, upload_to='media/images/', help_text='***** Update Auther Image Over Here *****')
    Blog_Post_Date = models.DateTimeField(null=True, blank=True, default=timezone.now)

    Introduction_Paragraph_1 = models.TextField(null=True, blank=True, default='Add Introduction Paragraph 1', help_text='***** Include Introduction Paragraph No. 1 *****')
    Introduction_Paragraph_2 = models.TextField(null=True, blank=True, default='Add Introduction Paragraph 2', help_text='***** Include Introduction Paragraph No. 2 *****')
    Introduction_Paragraph_3 = models.TextField(null=True, blank=True, default='Add Introduction Paragraph 3', help_text='***** Include Introduction Paragraph No. 3 *****')

    Some_Quotation = models.CharField(max_length=150, null=True, blank=True, default='Add Quotation', help_text='***** Include Your Quotation *****')

    Paragraph_1 = models.TextField(null=True, blank=True, default='Add Paragraph 1', help_text='***** Include Paragraph No. 1 *****')
    Paragraph_2 = models.TextField(null=True, blank=True, default='Add Paragraph 2', help_text='***** Include Paragraph No. 2 *****')
    Paragraph_3 = models.TextField(null=True, blank=True, default='Add Paragraph 3', help_text='***** Include Paragraph No. 3 *****')

    """-------------------------------- Section For HeadLine 1 --------------------------------"""

    Headline_1 = models.CharField(max_length=200, null=True, blank=True, default='Add Your HeadLine 1', help_text='***** Include HeadLine 1 *****')

    Headline_1_Paragraph_1 = models.TextField(null=True, blank=True, default='Add HeadLine 1 Paragraph 1', help_text='***** Include HeadLine 1 Paragraph No. 1 *****')
    Headline_1_Paragraph_2 = models.TextField(null=True, blank=True, default='Add HeadLine 1 Paragraph 2', help_text='***** Include HeadLine 1 Paragraph No. 2 *****')
    Headline_1_Paragraph_3 = models.TextField(null=True, blank=True, default='Add HeadLine 1 Paragraph 3', help_text='***** Include HeadLine 1 Paragraph No. 3 *****')

    Image_for_HeadLine_1 = models.ImageField(null=True, blank=True, upload_to='media/images/', help_text='***** Include Image for HeadLine 1 *****')
    Image_for_HeadLine_1_ALT_TAG = models.CharField(max_length=100, null=True, blank=True, default='Add Image ALT TAG', help_text='***** Include ALT TAG for that Image *****')

    """-------------------------------- Section For HeadLine 2 --------------------------------"""

    Headline_2 = models.CharField(max_length=200, null=True, blank=True, default='Add Your HeadLine 2', help_text='***** Include HeadLine 2 *****')

    Headline_2_Paragraph_1 = models.TextField(null=True, blank=True, default='Add HeadLine 2 Paragraph 1', help_text='***** Include HeadLine 2 Paragraph No. 1 *****')
    Headline_2_Paragraph_2 = models.TextField(null=True, blank=True, default='Add HeadLine 2 Paragraph 2', help_text='***** Include HeadLine 2 Paragraph No. 2 *****')
    Headline_2_Paragraph_3 = models.TextField(null=True, blank=True, default='Add HeadLine 2 Paragraph 3', help_text='***** Include HeadLine 2 Paragraph No. 3 *****')

    Image_for_HeadLine_2 = models.ImageField(null=True, blank=True, upload_to='media/images/', help_text='***** Include Image for HeadLine 2 *****')
    Image_for_HeadLine_2_ALT_TAG = models.CharField(max_length=100, null=True, blank=True, default='Add Image ALT TAG', help_text='***** Include ALT TAG for that Image *****')

    """-------------------------------- Section For HeadLine 3 --------------------------------"""

    Headline_3 = models.CharField(max_length=200, null=True, blank=True, default='Add Your HeadLine 3', help_text='***** Include HeadLine 3 *****')

    Headline_3_Paragraph_1 = models.TextField(null=True, blank=True, default='Add HeadLine 3 Paragraph 1', help_text='***** Include HeadLine 3 Paragraph No. 1 *****')
    Headline_3_Paragraph_2 = models.TextField(null=True, blank=True, default='Add HeadLine 3 Paragraph 2', help_text='***** Include HeadLine 3 Paragraph No. 2 *****')
    Headline_3_Paragraph_3 = models.TextField(null=True, blank=True, default='Add HeadLine 3 Paragraph 3', help_text='***** Include HeadLine 3 Paragraph No. 3 *****')

    Image_for_HeadLine_3 = models.ImageField(null=True, blank=True, upload_to='media/images/', help_text='***** Include Image for HeadLine 3 *****')
    Image_for_HeadLine_3_ALT_TAG = models.CharField(max_length=100, null=True, blank=True, default='Add Image ALT TAG', help_text='***** Include ALT TAG for that Image *****')

    Blog_Display_Status = models.BooleanField(null=False, blank=False, default=False, help_text='***** Check This box If you wanna Display this on your Web')

    def __str__(self):
        return f'{self.Blog_Title} by {self.Blog_Author} at {self.Blog_Date}'































