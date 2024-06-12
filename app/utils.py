def get_data(ancestor, selector, attribute=None, return_list=False):
    if return_list:
        return [tag.text.strip() for tag in ancestor.select(selector)]
    if attribute:
        if selector:
            try:
                return ancestor.select_one(selector)[attribute].strip()
            except TypeError:
                return None
        return ancestor[attribute].strip()
    try:
        return ancestor.select_one(selector).text.strip()
    except AttributeError:
        return None
    
selectors = {
    'opinion_id': (None, "data-entry-id"),
    'author': ("span.user-post__author-name",),
    'recommendation': ("span.user-post__author-recomendation > em",),
    'stars': ("span.user-post__score-count",),
    'content': ("div.user-post__text",),
    'pros': ("div.review-feature__title--positives ~ div.review-feature__item", None, True),
    'cons': ("div.review-feature__title--negatives ~ div.review-feature__item", None, True),
    'post_date': ("span.user-post__published > time:nth-child(1)", "datetime"),
    'purchase_date': ("span.user-post__published > time:nth-child(2)", "datetime"),
    'useful': ("button.vote-yes > span",),
    'useless': ("button.vote-no > span",),
}