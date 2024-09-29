from ..utils import clean_html


class Sections:

    @classmethod
    def final_html(cls,content_html):

        section_html = f'''
        <section>{content_html}</section>
        '''
        return clean_html(section_html)