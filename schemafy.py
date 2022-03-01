import re
raw = 'StructType(List(StructField(hvfhs_license_num,StringType,true),StructField(dispatching_base_num,StringType,true),StructField(pickup_datetime,StringType,true),StructField(dropoff_datetime,StringType,true),StructField(PULocationID,LongType,true),StructField(DOLocationID,LongType,true),StructField(SR_Flag,DoubleType,true)))'

def make_schema(raw):

    fields = []
    
    for i in zip([i.start() for i in re.finditer("\(",raw)][2:],[i.start() for i in re.finditer("\)",raw)][:-2]):
        fields.append(raw[i[0]+1:i[1]])

    schema = "types.StructType[\n"
    for f in fields:
        n = f.split(",")
        schema = schema+"\ttypes.StructField(\""+n[0]+"\", types."+n[1]+"(), "+n[2].capitalize()+")\n"
    schema = schema +"])"
    return schema
