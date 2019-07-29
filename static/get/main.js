function __init__(){
    numberOfInputs = 1;
}

function handler(){
    datasetInput = document.getElementById("datasetInput_id").value;
    hideOrShow1 = document.getElementById("specParmInput_key");
    hideOrShow1_label = document.getElementById("specParmInput_key_label");
    hideorShow2_label = document.getElementById("specParmInput_value_label");
    hideOrShow2 = document.getElementById("specParmInput_value");
    if (datasetInput == 'countries' || datasetInput == 'location_types'){
        hideOrShow1.style.display = 'none';
        hideOrShow2.style.display = 'none';
        hideOrShow1_label.style.display  = 'none';
        hideorShow2_label.style.display  = 'none';
        hideOrShow1.value= 'skip';
        hideOrShow2.value= 'skip';

    }
    else{
        hideOrShow1.style.display = 'block';
        hideOrShow2.style.display = 'block';
        hideOrShow1_label.style.display  = 'block';
        hideorShow2_label.style.display  = 'block';
        hideOrShow1.value = 'skip';
        hideOrShow2.value= 'skip';
    }

}

function showOrhideWidget(){
    if (document.getElementById("comparer_id").value == 1){
        document.getElementById("secondaryGrid").style.display = 'none';
    }
    else if (document.getElementById("comparer_id").value == 2){
        document.getElementById("secondaryGrid").style.display = 'block';
    }


}


__init__();