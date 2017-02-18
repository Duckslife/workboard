from django.shortcuts import render_to_response
from django.utils import timezone
from workboard.models import workboard
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from workboard.pagingHelper import pagingHelper

rowsPerPage = 2

'''@csrf_exempt'''
def home(request):
	boardList = workboard.objects.order_by('-id')[0:2]
	current_page = 1
	totalCnt = workboard.objects.all().count()
	
	pagingHelperIns = pagingHelper();
	
	totalPageList = pagingHelperIns.getTotalPageList(totalCnt,rowsPerPage)
	print 'totalPageList', totalPageList

	return render_to_response('listSpecificPage.html', {'boardList': boardList, 'totalCnt': totalCnt, 
                                                        'current_page':current_page ,'totalPageList':totalPageList} ) 

