function __init__(){
    if (window.performance) {
        console.info("window.performance works fine on this browser");
      }
        if (performance.navigation.type == 1) {
          console.info( "This page is reloaded" );
          location.href = "/";
        } else {
          console.info( "This page is not reloaded");
        }
}

function handler(index){
    datasetInput = document.getElementById("datasetInput_id" + index).value;
    specValue = document.getElementById("specParmInput_value" + index);
    specKey = document.getElementById("specParmInput_key" + index);


    if (datasetInput == 'countries' || datasetInput == 'location_types'){
        specValue.readOnly = true;
        specKey.readOnly = true; 
        specValue.value='skip';
        specKey.value='skip';

    }
    else{
        specValue.readOnly = false;
        specKey.readOnly = false; 
    }

}

function showOrhideWidget(){
    hideOrShowSecondaryInput = document.getElementById("secondaryGrid");
    hideOrShowThirdInput = document.getElementById("thirdGrid");

    if (document.getElementById("comparer_id").value == 1){
        hideOrShowSecondaryInput.style.display = 'none';
        hideOrShowThirdInput.style.display = 'none';
    }
    else if (document.getElementById("comparer_id").value == 2){
        hideOrShowSecondaryInput.style.display = 'block';
        hideOrShowThirdInput.style.display = 'none';
    }
    else if (document.getElementById("comparer_id").value == 3){
        hideOrShowSecondaryInput.style.display = 'block';
        hideOrShowThirdInput.style.display = 'block';
    }


}

function returnValidation() {

    datasetChoice1 = document.getElementById("datasetInput_id1").value;
    datasetChoice2 = document.getElementById("datasetInput_id2").value;
    datasetChoice3 = document.getElementById("datasetInput_id3").value;

    if ((datasetChoice1 == datasetChoice2) && document.getElementById("comparer_id").value  >=2){
        document.getElementById("errorMessage").innerHTML = "Datasets must be unique. Dataset 1 and 2 are the same.";
        return false;
    } 
    else if ((datasetChoice1 == datasetChoice3) && document.getElementById("comparer_id").value ==3){
        document.getElementById("errorMessage").innerHTML = "Datasets must be unique. Dataset 1 and 3 are the same";
        return false;
    } 
    else if ((datasetChoice2 == datasetChoice3) && document.getElementById("comparer_id").value ==3){
        document.getElementById("errorMessage").innerHTML = "Datasets must be unique. Dataset 2 and 3 are the same";
        return false;
    } 
    return true;
}


__init__();