from django.db import models

class Intake(models.Model):
    #id = models.CharField(max_length=50, unique=True)
    #user = models.ForeignKey(SurveyUser)
    global_id = models.CharField(max_length=36, unique=True)
    channel = models.CharField(max_length=36, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    TITLE_1 = models.TextField()
    NOTE_1 = models.TextField()
    NOTE_2 = models.TextField()
    TITLE_2 = models.TextField()
    QUESTION_1 = models.TextField()
    TITLE_3 = models.TextField()
    QUESTION_2_multi_row1_col1 = models.SmallIntegerField()
    QUESTION_2_multi_row1_col2 = models.SmallIntegerField()
    QUESTION_2_multi_row1_col3 = models.SmallIntegerField()
    QUESTION_2_multi_row2_col1 = models.SmallIntegerField()
    QUESTION_2_multi_row2_col2 = models.SmallIntegerField()
    QUESTION_2_multi_row2_col3 = models.SmallIntegerField()
    QUESTION_2_multi_row3_col1 = models.SmallIntegerField()
    QUESTION_2_multi_row3_col2 = models.SmallIntegerField()
    QUESTION_2_multi_row3_col3 = models.SmallIntegerField()
    QUESTION_2_multi_row4_col1 = models.SmallIntegerField()
    QUESTION_2_multi_row4_col2 = models.SmallIntegerField()
    QUESTION_2_multi_row4_col3 = models.SmallIntegerField()
    QUESTION_2_multi_row5_col1 = models.SmallIntegerField()
    QUESTION_2_multi_row5_col2 = models.SmallIntegerField()
    QUESTION_2_multi_row5_col3 = models.SmallIntegerField()
    QUESTION_2_multi_row6_col1 = models.SmallIntegerField()
    QUESTION_2_multi_row6_col2 = models.SmallIntegerField()
    QUESTION_2_multi_row6_col3 = models.SmallIntegerField()
    QUESTION_2_multi_row7_col1 = models.SmallIntegerField()
    QUESTION_2_multi_row7_col2 = models.SmallIntegerField()
    QUESTION_2_multi_row7_col3 = models.SmallIntegerField()
    QUESTION_2_multi_row8_col1 = models.SmallIntegerField()
    QUESTION_2_multi_row8_col2 = models.SmallIntegerField()
    QUESTION_2_multi_row8_col3 = models.SmallIntegerField()
    QUESTION_2_multi_row9_col1 = models.SmallIntegerField()
    QUESTION_2_multi_row9_col2 = models.SmallIntegerField()
    QUESTION_2_multi_row9_col3 = models.SmallIntegerField()
    QUESTION_2_multi_row10_col1 = models.SmallIntegerField()
    QUESTION_2_multi_row10_col2 = models.SmallIntegerField()
    QUESTION_2_multi_row10_col3 = models.SmallIntegerField()
    QUESTION_2_multi_row11_col1 = models.SmallIntegerField()
    QUESTION_2_multi_row11_col2 = models.SmallIntegerField()
    QUESTION_2_multi_row11_col3 = models.SmallIntegerField()
    QUESTION_2_multi_row12_col1 = models.SmallIntegerField()
    QUESTION_2_multi_row12_col2 = models.SmallIntegerField()
    QUESTION_2_multi_row12_col3 = models.SmallIntegerField()
    TITLE_4= models.BooleanField(default=False)
    QUESTION_3 = models.CharField(max_length=30, null=True)
    QUESTION_4_0= models.BooleanField(default=False)
    QUESTION_4_0_open= models.SmallIntegerField()
    QUESTION_4_1= models.BooleanField(default=False)
    QUESTION_4_1_open= models.SmallIntegerField()
    QUESTION_4_2= models.BooleanField(default=False)
    QUESTION_4_2_open= models.SmallIntegerField()
    TITLE_5= models.BooleanField(default=False)
    QUESTION_5_multi_row1_col1= models.SmallIntegerField()
    QUESTION_5_multi_row1_col2= models.SmallIntegerField()
    QUESTION_5_multi_row1_col3= models.SmallIntegerField()
    QUESTION_5_multi_row1_col4= models.SmallIntegerField()
    QUESTION_5_multi_row1_col5= models.SmallIntegerField()
    QUESTION_5_multi_row1_col6= models.SmallIntegerField()
    QUESTION_5_multi_row2_col1= models.SmallIntegerField()
    QUESTION_5_multi_row2_col2= models.SmallIntegerField()
    QUESTION_5_multi_row2_col3= models.SmallIntegerField()
    QUESTION_5_multi_row2_col4= models.SmallIntegerField()
    QUESTION_5_multi_row2_col5= models.SmallIntegerField()
    QUESTION_5_multi_row2_col6= models.SmallIntegerField()
    QUESTION_5_multi_row3_col1= models.SmallIntegerField()
    QUESTION_5_multi_row3_col2= models.SmallIntegerField()
    QUESTION_5_multi_row3_col3= models.SmallIntegerField()
    QUESTION_5_multi_row3_col4= models.SmallIntegerField()
    QUESTION_5_multi_row3_col5= models.SmallIntegerField()
    QUESTION_5_multi_row3_col6= models.SmallIntegerField()
    QUESTION_5_multi_row4_col1= models.SmallIntegerField()
    QUESTION_5_multi_row4_col2= models.SmallIntegerField()
    QUESTION_5_multi_row4_col3= models.SmallIntegerField()
    QUESTION_5_multi_row4_col4= models.SmallIntegerField()
    QUESTION_5_multi_row4_col5= models.SmallIntegerField()
    QUESTION_5_multi_row4_col6= models.SmallIntegerField()
    QUESTION_5_multi_row5_col1= models.SmallIntegerField()
    QUESTION_5_multi_row5_col2= models.SmallIntegerField()
    QUESTION_5_multi_row5_col3= models.SmallIntegerField()
    QUESTION_5_multi_row5_col4= models.SmallIntegerField()
    QUESTION_5_multi_row5_col5= models.SmallIntegerField()
    QUESTION_5_multi_row5_col6= models.SmallIntegerField()
    QUESTION_5_multi_row6_col1= models.SmallIntegerField()
    QUESTION_5_multi_row6_col2= models.SmallIntegerField()
    QUESTION_5_multi_row6_col3= models.SmallIntegerField()
    QUESTION_5_multi_row6_col4= models.SmallIntegerField()
    QUESTION_5_multi_row6_col5= models.SmallIntegerField()
    QUESTION_5_multi_row6_col6= models.SmallIntegerField()
    QUESTION_5_multi_row7_col1= models.SmallIntegerField()
    QUESTION_5_multi_row6_col2= models.SmallIntegerField()
    QUESTION_5_multi_row6_col3= models.SmallIntegerField()
    QUESTION_5_multi_row6_col4= models.SmallIntegerField()
    QUESTION_5_multi_row6_col5= models.SmallIntegerField()
    QUESTION_5_multi_row6_col6= models.SmallIntegerField()
    QUESTION_5_multi_row7_col1= models.SmallIntegerField()
    QUESTION_5_multi_row7_col2= models.SmallIntegerField()
    QUESTION_5_multi_row7_col3= models.SmallIntegerField()
    QUESTION_5_multi_row7_col4= models.SmallIntegerField()
    QUESTION_5_multi_row7_col5= models.SmallIntegerField()
    QUESTION_5_multi_row7_col6= models.SmallIntegerField()
    TITLE_6= models.BooleanField(default=False)
    QUESTION_6= models.SmallIntegerField()
    QUESTION_7= models.SmallIntegerField()
    QUESTION_8= models.SmallIntegerField()
    QUESTION_9_0= models.BooleanField(default=False)
    QUESTION_9_0_open= models.SmallIntegerField()
    QUESTION_9_1= models.BooleanField(default=False)
    QUESTION_9_1_open= models.SmallIntegerField()
    QUESTION_9_2= models.BooleanField(default=False)
    QUESTION_9_2_open= models.SmallIntegerField()
    QUESTION_9_3= models.BooleanField(default=False)
    QUESTION_9_3_open= models.SmallIntegerField()
    QUESTION_9_4= models.BooleanField(default=False)
    QUESTION_9_4_open= models.SmallIntegerField()
    QUESTION_10_multi_row1_col1= models.BooleanField(default=False)
    QUESTION_10_multi_row2_col1= models.BooleanField(default=False)
    QUESTION_10_multi_row3_col1= models.BooleanField(default=False)
    QUESTION_10_multi_row4_col1= models.BooleanField(default=False)
    QUESTION_11= models.BooleanField(default=False)
    QUESTION_12_multi_row1_col1= models.BooleanField(default=False)
    QUESTION_12_multi_row2_col1= models.BooleanField(default=False)
    QUESTION_12_multi_row3_col1= models.BooleanField(default=False)
    QUESTION_12_multi_row4_col1= models.BooleanField(default=False)
    QUESTION_12_multi_row5_col1= models.BooleanField(default=False)
    QUESTION_13_multi_row1_col1= models.BooleanField(default=False)
    QUESTION_13_multi_row2_col1= models.BooleanField(default=False)
    QUESTION_13_multi_row3_col1= models.BooleanField(default=False)
    QUESTION_13_multi_row4_col1= models.BooleanField(default=False)
    QUESTION_13_multi_row5_col1= models.BooleanField(default=False)
    QUESTION_14_multi_row1_col1= models.SmallIntegerField()
    QUESTION_14_multi_row1_col2= models.SmallIntegerField()
    QUESTION_14_multi_row1_col3= models.SmallIntegerField()
    QUESTION_14_multi_row1_col4= models.SmallIntegerField()
    QUESTION_14_multi_row2_col1= models.SmallIntegerField()
    QUESTION_14_multi_row2_col2= models.SmallIntegerField()
    QUESTION_14_multi_row2_col3= models.SmallIntegerField()
    QUESTION_14_multi_row2_col4= models.SmallIntegerField()
    QUESTION_14_multi_row3_col1= models.SmallIntegerField()
    QUESTION_14_multi_row3_col2= models.SmallIntegerField()
    QUESTION_14_multi_row3_col3= models.SmallIntegerField()
    QUESTION_14_multi_row3_col4= models.SmallIntegerField()
    QUESTION_14_multi_row4_col1= models.SmallIntegerField()
    QUESTION_14_multi_row4_col2= models.SmallIntegerField()
    QUESTION_14_multi_row4_col3= models.SmallIntegerField()
    QUESTION_14_multi_row4_col4= models.SmallIntegerField()
    QUESTION_14_multi_row5_col1= models.SmallIntegerField()
    QUESTION_14_multi_row5_col2= models.SmallIntegerField()
    QUESTION_14_multi_row5_col3= models.SmallIntegerField()
    QUESTION_14_multi_row5_col4= models.SmallIntegerField()
    TITLE_7= models.BooleanField(default=False)
    QUESTION_15= models.SmallIntegerField()
    QUESTION_16= models.SmallIntegerField()
    QUESTION_17= models.SmallIntegerField()
    QUESTION_18_multi_row1_col1= models.SmallIntegerField()
    QUESTION_18_multi_row2_col1= models.SmallIntegerField()
    QUESTION_18_multi_row3_col1= models.SmallIntegerField()
    QUESTION_19= models.SmallIntegerField()
    QUESTION_20_multi_row1_col1= models.SmallIntegerField()
    QUESTION_20_multi_row2_col1= models.SmallIntegerField()
    QUESTION_20_multi_row3_col1= models.SmallIntegerField()
    QUESTION_21= models.SmallIntegerField()
    QUESTION_22_multi_row1_col1= models.SmallIntegerField()
    QUESTION_22_multi_row1_col2= models.SmallIntegerField()
    QUESTION_22_multi_row2_col1= models.SmallIntegerField()
    QUESTION_22_multi_row2_col2= models.SmallIntegerField()
    QUESTION_22_multi_row3_col1= models.SmallIntegerField()
    QUESTION_22_multi_row3_col2= models.SmallIntegerField()
    QUESTION_22_multi_row4_col1= models.SmallIntegerField()
    QUESTION_22_multi_row4_col2= models.SmallIntegerField()
    QUESTION_22_multi_row5_col1= models.SmallIntegerField()
    QUESTION_22_multi_row5_col2= models.SmallIntegerField()
    QUESTION_22_multi_row6_col1= models.SmallIntegerField()
    QUESTION_22_multi_row6_col2= models.SmallIntegerField()
    QUESTION_23= models.SmallIntegerField()
    QUESTION_24= models.SmallIntegerField()
    QUESTION_25= models.SmallIntegerField()
    TITLE_8= models.BooleanField(default=False)
    QUESTION_26= models.SmallIntegerField()
    QUESTION_27_multi_row1_col1= models.SmallIntegerField()
    QUESTION_27_multi_row2_col1= models.SmallIntegerField()
    QUESTION_27_multi_row3_col1= models.SmallIntegerField()
    TITLE_9= models.BooleanField(default=False)
    QUESTION_28= models.SmallIntegerField()
    QUESTION_29= models.BooleanField(default=False)
    QUESTION_30_multi_row1_col1= models.SmallIntegerField()
    QUESTION_30_multi_row1_col2= models.SmallIntegerField()
    QUESTION_30_multi_row2_col1= models.SmallIntegerField()
    QUESTION_30_multi_row2_col2= models.SmallIntegerField()
    QUESTION_30_multi_row3_col1= models.SmallIntegerField()
    QUESTION_30_multi_row3_col2= models.SmallIntegerField()
    QUESTION_30_multi_row4_col1= models.SmallIntegerField()
    QUESTION_30_multi_row4_col2= models.SmallIntegerField()
    QUESTION_30_multi_row5_col1= models.SmallIntegerField()
    QUESTION_30_multi_row5_col2= models.SmallIntegerField()
    QUESTION_30_multi_row6_col1= models.SmallIntegerField()
    QUESTION_30_multi_row6_col2= models.SmallIntegerField()
    QUESTION_31= models.SmallIntegerField()
    QUESTION_32= models.SmallIntegerField()
    QUESTION_33= models.SmallIntegerField()
    QUESTION_34= models.SmallIntegerField()

    class Meta:
        db_table = "pollster_results_intake_zoe"
        managed = False

    def __unicode__(self):
        #return '%s - %s' % (self.id, self.TITLE_1)
        return '%s' % self.id

    class Meta:
        verbose_name_plural = 'Survey Participation Intake'