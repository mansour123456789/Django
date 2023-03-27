import io, csv
from concurrent.futures.thread import _worker
from django.shortcuts import get_object_or_404, render
from requests import post
from .forms import NameForm
from .models import FileMs
from .models import File
from .models import rute

from tablib import Dataset
from .resource import modelresource
import pandas as pd 
import psycopg2 

# Create your views here.

def condition(request):
    

    return render(request,'dashboard/condition.html'  )




def rutee(request):
    context = {}

    if request.method== 'POST':

       
        rutee=request.POST['rute']
        aa=  rute.objects.create(name=rutee)
        all=rute.objects.all()
        context['data']=all
        
        return render(request,'dashboard/rute.html',context  )
    

    all=rute.objects.all()
    context['data']=all
   
    return render(request,'dashboard/rute.html',context )

def aa(request):
    context = {}
   
    return render(request,'dashboard/rute.html',context )






 

def table(request,id):
    context = {}
    d=FileMs.objects.filter(file_id=128)
    context['data']=d
    return render(request,'dashboard/import.html',context )





def file(request):
    context = {}
    file=File.objects.all()
    context['data']=file
    return render(request,'dashboard/file.html',context )












def upload(request):
    context = {}
    template = "dashboard/upload_file.html"


    if request.method == "GET":

        
        return render(request , 'dashboard/upload_file.html', context)
    
    
    if request.method== 'POST':
        
        file=request.FILES['my_file']
        



        
        
        conn=psycopg2.connect(host='localhost',dbname='projet',user='postgres',password='123456789',port='5432')
        import_ms_file(file,conn)        
        
    return render(request , 'dashboard/file.html' , context)




def import_ms_file (file,conn):
    #read file pandas
    connn=psycopg2.connect(host='localhost',dbname='projet',user='postgres',password='123456789',port='5432')
    ll= File.objects.create(name=file)
    ll.save()
    dc=pd.read_excel(file)
    f=dc
  
    
 

    # msfile=io.StringIO()
    # t=dc.to_csv(index=None,header=None)
    # with open(t, 'r') as read_obj, 
    #     open('output_1.csv', 'w', newline='') as write_obj:
    # # Create a csv.reader object from the input file object
            #   csv_reader = csv.reader(read_obj)
    # Create a csv.writer object from the output file object
            #   csv_writer = csv.writer(write_obj)
    # Read each row of the input csv file as list
            #   for row in csv_reader:
        # Append the default text in the row / list
                #    row.append('aaaaaaaaa')
        # Add the updated row / list to the output file
                #    csv_writer.writerow(row)
    
    filee=pd.DataFrame(f)
  
    filee.loc[:,'file_id']=ll.id
   
    # filee.insert(loc=0, column="file_id", value=ll.pk)
    # msfile.seek(0)
    msfilee=io.StringIO()
    msfilee.write(filee.to_csv(index=None,header=None))
    msfilee.seek(0)
    
    print(filee)
    print("///////////////////////////////")

    msfilee.seek(0)
    print(msfilee.read())
      
    msfilee.seek(0)
     

    with connn.cursor() as c:
            vall=ll.name,
            
            c.copy_from(
           
            file=msfilee,
            table="profil_filems",
            
            columns=[
       
       'article',
       'designation_article',
       'text_article',
       'grpe_march',
       'div',
       'ctrpr',
       'typ_app',
       'a_s',
       'tcy',
       'dfi',
       'dpr',
       'horiz',
       'mp',
       'r',
       'tyar',
       'nal',
       'i_c',
       'aappr_def',
       'mgapp',
       'mag',
       'tl',
       'lot_fixe',
       'uq1',
       'stock_securite',
       'uq0',
       'tre',
       'gest',
       'di',    
       'rebut',
       'gac',
       'Profil',
       'prpiAt',
       'cree_par',
       'langue',
       'Cree_le',
       'gcha',
       'gs',
       'mode_de_comparaison_des_besoin',
       'int_ajust_amont',
       'int_ajust_aval',
       'taille_l_min',
       'uq2',
       'val_arrondie',
       'uq3',
       'taille_lot_mx',
       'uq4',
       'stock_maximum',
       'uq5',
       'chant',
       'typ',
       'delai_sec',
       'delai_sec1',
       'ctrl_destinataire',
       'article_rempl',
       'dv',
       'gml',
       'grpl',
       'abc',
       'uq6',
       'element_dOTP',
       'grpa',
       'Code_pilotage',
       'hierarch_produits',
       'poids_brut',
       'unp1',
       'poids_net',
       'unp2',
       'pas_de_ccr',
       'Taille_de_lot_du_CCR',
       'uq7',
       'file_id'
       
       

        ],
        null="",
        sep=",",
        
        

        ),
    
            
             
            
    connn.commit()
    
    







# def update(request,id):
#     context = {}

    
    
#     ll= file.objects.filter(id=id)
#     lignee=rute.objects.filter(id_file=id)
#     context['data'] =  lignee
#     context['idd'] =  id
#     i=mansour.objects.filter(id_file=ll.get())
#     for choi in lignee:
#         for lign in i:
#             if choi.choix=="age" :
#                 lign.age=choi.condition
#             if choi.choix=="color" :
#                 lign.color=choi.condition  
#             if choi.choix=="name" :
#                 lign.name=choi.condition      
    
    
#     context['ligne']=i
    
    
#     return render(request , 'dashboard/kkk.html', context)









# def choix(request ,id):
#     context = {}

    
    
#     ll= file.objects.filter(id=id)
#     lignee=condition.objects.filter(id_file=id)
#     context['data'] =  lignee
#     context['idd'] =  id
   
#     if request.method == "GET":
#         return render(request , 'dashboard/condition.html', context)

#     return render(request , 'dashboard/condition.html' , context)



# def conditionn(request ,id):
#      context = {}

    
    
     
#      context['idd'] =  id
#      if request.method== 'POST':
#          form = NameForm(request.POST)
#          l=form.data["condition"]
#          s=form.data["choix"]
#          ll= file.objects.filter(id=id).get()
         
#          co=condition.objects.create(condition=l,choix=s,id_file=ll)

#          co.save()



#      return render(request , 'dashboard/formcondition.html', context)









# def importExcel(request,id):
#     context = {}
#     template = "dashboard/import.html"
   
#     data = mansour.objects.all()
    
#     ll= file.objects.filter(id=id)
#     lignee=mansour.objects.filter(id_file=id)
#     context['data'] =  lignee
#     context['idd'] =  id
   
#     if request.method == "GET":
#         return render(request , 'dashboard/import.html', context)
    

#     return render(request,'dashboard/import.html')












