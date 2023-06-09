from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.













class File (models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField( max_length=50,null=False,blank=True)
    imported_by =models.CharField( max_length=50,null=True,blank=True)
    timestamp        = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated          = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return str(self.id)

    
    
    








class FileMs(models.Model):
    
    article= models.CharField( max_length=50,null=True,blank=True)
    designation_article= models.CharField( max_length=50,null=True,blank=True)
    text_article= models.CharField( max_length=50,null=True,blank=True)
    grpe_march= models.CharField( max_length=50,null=True,blank=True)
    div= models.CharField( max_length=50,null=True,blank=True)
    ctrpr= models.CharField( max_length=50,null=True,blank=True)
    typ_app= models.CharField( max_length=50,null=True,blank=True)
    a_s= models.CharField( max_length=50,null=True,blank=True)
    tcy= models.CharField( max_length=50,null=True,blank=True)
    dfi= models.CharField( max_length=50,null=True,blank=True)
    dpr= models.CharField( max_length=50,null=True,blank=True)
    horiz= models.CharField( max_length=50,null=True,blank=True)
    mp= models.CharField( max_length=50,null=True,blank=True)
    r= models.CharField( max_length=50,null=True,blank=True)
    tyar= models.CharField( max_length=50,null=True,blank=True)
    nal= models.CharField( max_length=50,null=True,blank=True)
    i_c= models.CharField( max_length=50,null=True,blank=True)
    aappr_def= models.CharField( max_length=50,null=True,blank=True)
    mgapp= models.CharField( max_length=50,null=True,blank=True)
    mag= models.CharField( max_length=50,null=True,blank=True)
    tl= models.CharField( max_length=50,null=True,blank=True)
    lot_fixe= models.CharField( max_length=50,null=True,blank=True)
    uq1= models.CharField( max_length=50,null=True,blank=True)
    stock_securite= models.CharField( max_length=50,null=True,blank=True)
    uq0= models.CharField( max_length=50,null=True,blank=True)
   
    tre= models.CharField( max_length=50,null=True,blank=True)
    gest= models.CharField( max_length=50,null=True,blank=True)
    di= models.CharField( max_length=50,null=True,blank=True) 
    rebut= models.CharField( max_length=50,null=True,blank=True)
    gac= models.CharField( max_length=50,null=True,blank=True)
    Profil= models.CharField( max_length=50,null=True,blank=True)
    prpiAt= models.CharField( max_length=50,null=True,blank=True)
    cree_par= models.CharField( max_length=50,null=True,blank=True)
    langue= models.CharField( max_length=50,null=True,blank=True)
    Cree_le= models.CharField( max_length=50,null=True,blank=True)
    gcha= models.CharField( max_length=50,null=True,blank=True)
    gs=models.CharField( max_length=50,null=True,blank=True)
    mode_de_comparaison_des_besoin= models.CharField( max_length=50,null=True,blank=True)
    int_ajust_amont= models.CharField( max_length=50,null=True,blank=True)
    int_ajust_aval= models.CharField( max_length=50,null=True,blank=True)
    taille_l_min= models.CharField( max_length=50,null=True,blank=True)
    uq2= models.CharField( max_length=50,null=True,blank=True)
    val_arrondie= models.CharField( max_length=50,null=True,blank=True)
    uq3= models.CharField( max_length=50,null=True,blank=True)
    taille_lot_mx= models.CharField( max_length=50,null=True,blank=True)
    uq4= models.CharField( max_length=50,null=True,blank=True)
    stock_maximum= models.CharField( max_length=50,null=True,blank=True)
    uq5= models.CharField( max_length=50,null=True,blank=True)
    chant= models.CharField( max_length=50,null=True,blank=True)
    typ= models.CharField( max_length=50,null=True,blank=True)
    delai_sec= models.CharField( max_length=50,null=True,blank=True)
    delai_sec1= models.CharField( max_length=50,null=True,blank=True)
    ctrl_destinataire= models.CharField( max_length=50,null=True,blank=True)
    article_rempl= models.CharField( max_length=50,null=True,blank=True)
    dv= models.CharField( max_length=50,null=True,blank=True)
    gml= models.CharField( max_length=50,null=True,blank=True)
    grpl= models.CharField( max_length=50,null=True,blank=True)
    abc= models.CharField( max_length=50,null=True,blank=True)
    uq6= models.CharField( max_length=50,null=True,blank=True)
    element_dOTP= models.CharField( max_length=50,null=True,blank=True)
    grpa= models.CharField( max_length=50,null=True,blank=True)
    Code_pilotage= models.CharField( max_length=50,null=True,blank=True)
    hierarch_produits= models.CharField( max_length=50,null=True,blank=True)
    poids_brut= models.CharField( max_length=50,null=True,blank=True)
    unp1= models.CharField( max_length=50,null=True,blank=True)
    poids_net= models.CharField( max_length=50,null=True,blank=True)
    unp2= models.CharField( max_length=50,null=True,blank=True)
    pas_de_ccr= models.CharField( max_length=50,null=True,blank=True)
    Taille_de_lot_du_CCR= models.CharField( max_length=50,null=True,blank=True)
    uq7= models.CharField( max_length=50,null=True,blank=True)
    file_id=models.CharField( max_length=50,null=True,blank=True)
   
       
    def __str__(self):
        return self.article



class rute (models.Model):
   
    name=models.CharField( max_length=50,null=True,blank=True)
    imported_by=models.CharField( max_length=50,null=True,blank=True)
    date        = models.DateTimeField(auto_now=False,auto_now_add=True)
    
   

class condition (models.Model):
    
    field=models.CharField( max_length=50,null=True,blank=True)
    Con=models.CharField( max_length=50,null=True,blank=True)
    id_rute=models.ForeignKey(rute, on_delete=models.CASCADE)


class resulta (models.Model):
    
    field=models.CharField( max_length=50,null=True,blank=True)
    Res=models.CharField( max_length=50,null=True,blank=True)
    id_condition=models.ForeignKey(condition, on_delete=models.CASCADE)



class lm (models.Model):
    
    field=models.CharField( max_length=50,null=True,blank=True)
    vieux=models.CharField( max_length=50,null=True,blank=True)
    nouveau=models.CharField( max_length=50,null=True,blank=True)
    id_condition=models.ForeignKey(condition, on_delete=models.CASCADE)
    id_ligne=models.ForeignKey(FileMs, on_delete=models.CASCADE)
    id_file=models.ForeignKey(File, on_delete=models.CASCADE)
    




