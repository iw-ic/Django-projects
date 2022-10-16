from django.http import HttpResponse
from django.shortcuts import render
import operator


def Homepage(request):
    return render(request, "home.html")
    # return HttpResponse("hello world")


def Count(request):
    fulltext = request.GET["fulltext"]
    wordlist = fulltext.split()
    wordcount_dict = {}
    for word in wordlist:
        if word in wordcount_dict.keys():
            wordcount_dict[word] = wordcount_dict[word] + 1
        else:
            wordcount_dict[word] = 1
    return render(
        request,
        "count.html",
        {
            "fulltext": fulltext,
            "wordcount": len(wordlist),
            "unique_word_count": len(wordcount_dict),
            "wordcount_dict": sorted(
                wordcount_dict.items(), key=operator.itemgetter(1), reverse=True
            ),
        },
    )


def about(request):
    return render(request, "about.html")
