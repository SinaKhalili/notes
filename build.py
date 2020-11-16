#!/usr/bin/env python3

import os
import re

from lettersmith.lens import put
from lettersmith import doc as Doc
from lettersmith import *
import config

environment = os.getenv('BUILD_ENV', 'development')
build_config = config.deploy if environment == 'deploy' else config.development

base_url = build_config.base_url
print('Base url is {}'.format(base_url))

site_title = 'Mind excursions'

static = files.find('static/**/*')

pages = pipe(
    docs.find('**/*.md'),
    docs.remove_index,
    docs.remove_drafts,
    permalink.rel_page_permalink('.'),
    docs.uplift_frontmatter,
    docs.with_template('page.html'),
)

home = pipe(
    docs.find('index.md'),
    permalink.rel_page_permalink('.'),
    docs.uplift_frontmatter,
    docs.with_template('page.html'),
)

def remove_double_hrefs(docs):
    """
    Removes double href-ing of links
    """
    for doc in docs:
        yield put(
            Doc.content, 
            doc, 
            re.sub(
                r'<a href=\"http.+?<a href=\"(http.*?)\">\1</a>\"', 
                r'<a href="\1"', 
                doc.content,
            )
        )

all_pages = pipe(
    (*pages, *home),
    wikidoc.content_markdown(base_url),
    absolutize.absolutize(base_url),
    remove_double_hrefs,
)

context = {
    'site': {
        'title': site_title,
    },
    'base_url': base_url
}

rendered_docs = pipe(
    (all_pages),
    jinjatools.jinja('templates', base_url, context)
)

write(chain(static, rendered_docs), directory='public')

print('Done!')
