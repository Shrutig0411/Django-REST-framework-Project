from django.db import models
from pygments import highlight
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    # set value when object is first saved
    created = models.DateTimeField(auto_now_add=True)
    # blank = True means field will not be required, if false then field cannot be blank
    title = models.CharField(max_length=255, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)

    # in the following 2 fields choices concept is being used, sequence of two-tuple is reqd as follows

    language = models.CharField(
        choices=LANGUAGE_CHOICES, default='python', max_length=255)
    style = models.CharField(choices=STYLE_CHOICES,
                             default='friendly', max_length=255)

    # fields for auth
    # related name is for reverse relation from the user model back to our model
    owner = models.ForeignKey(
        'auth.User', related_name='snippets', on_delete=models.CASCADE)

    # will be used for storing highlighted HTML representation of the code
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        '''
        Uses the pygments library to create a highlighted HTML
        representation of the code snippet
        '''
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created']  # default ordering when objects are fetched
