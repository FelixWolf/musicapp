integer STATE_INVENTORY = 0;
integer STATE_READY = 1;
integer STATE_UPLOAD = 2;
integer STATE_FINISHED = 3;

integer gIsSelfModifying;
integer gState;
key gUploadReq;

beginUpload(){
    //Only need sounds and images
    list sounds;
    integer i;
    integer l = llGetInventoryNumber(INVENTORY_SOUND);
    for(;i<l;i++){
        string n = llGetInventoryName(INVENTORY_SOUND, i);
        sounds += [
            n,
            llGetInventoryKey(n)
        ];
    }
    list textures;
    l = llGetInventoryNumber(INVENTORY_TEXTURE);
    for(i=0;i<l;i++){
        string n = llGetInventoryName(INVENTORY_TEXTURE, i);
        textures += [
            n,
            llGetInventoryKey(n)
        ];
    }
    gUploadReq = llHTTPRequest("https://musicapp.apps.softhyena.com/api/upload", [
        HTTP_METHOD, "POST",
        HTTP_VERIFY_CERT, FALSE
    ], llList2Json(JSON_OBJECT, [
        "sounds", llList2Json(JSON_OBJECT, sounds),
        "textures", llList2Json(JSON_OBJECT, textures)
    ]));
}

default{
    state_entry(){
        llSetLinkPrimitiveParamsFast(2, [
            PRIM_OMEGA, <0,0,1>, 1, 1
        ]);
        llSetTextureAnim(ANIM_ON | LOOP | REVERSE, 0, 1, 4, 0.0, 4.0, 3.2);
        llSetText("Waiting for inventory...", <1,1,1>, 1);
        gState = STATE_INVENTORY;
    }

    changed(integer c){
        if(c&CHANGED_INVENTORY){
            if(!gIsSelfModifying){
                gState = STATE_INVENTORY;
                llSetText("Processing inventory drop!\n"
                +(string)llGetInventoryNumber(INVENTORY_SOUND)+" Sample(s)\n"
                +(string)llGetInventoryNumber(INVENTORY_TEXTURE)+" Album(s) art", <1,1,0>, 1);
                llSetTimerEvent(1);
            }
        }   
    }
    
    timer(){
        llSetTimerEvent(0);
        if(llGetInventoryNumber(INVENTORY_SOUND) == 0)
            llResetScript();
        llSetText("Ready for upload!\n"
            +(string)llGetInventoryNumber(INVENTORY_SOUND)+" Sample(s)\n"
             +(string)llGetInventoryNumber(INVENTORY_TEXTURE)+" Album(s) art", <0,1,0>, 1);
        gState = STATE_READY;
    }
    
    touch_start(integer dt){
        while(dt--){
            if(llDetectedKey(dt) == llGetOwner()){
                if(gState == STATE_READY){
                    beginUpload();   
                    gState = STATE_UPLOAD;
                    llSetText("Uploading...\n"
                        +(string)llGetInventoryNumber(INVENTORY_SOUND)+" Sample(s)\n"
                         +(string)llGetInventoryNumber(INVENTORY_TEXTURE)+" Album(s) art", <1,1,0>, 1);
                }else{
                    llOwnerSay("Please add sounds and textures to me, then try clicking me!");   
                }
            }   
        }
    }
    
    http_response(key id, integer status, list meta, string data){
        if(id == gUploadReq){
            if(status == 200){
                //Server will send a fully qualified URL
                llLoadURL(llGetOwner(), "Upload ready!", data);   
                gState = STATE_FINISHED;
            }else{
                llOwnerSay("Oops! Upload failed:\nStatus: "+(string)status+"\n"+data);
                llOwnerSay("Click to try again.");
            }
        }   
    }
}
