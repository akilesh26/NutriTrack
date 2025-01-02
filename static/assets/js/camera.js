(()=>{
    const video = document.getElementById("video");
    const captureButton = document.getElementById("click");

    const streaming = false;

    let width = 500;
    let height = 500;

    navigator.mediaDevices
        .getUserMedia({video:true, audio:false})
        .then(
            (stream) => {
                video.srcObject=stream;
                video.play();
            }
        )
        .catch(
            (err) => {
                video.innerText = "Camera not Available."
            }
        );

        captureButton.addEventListener(
            "click",
            (ev) => {
                takePicture();  
                ev.preventDefault();
            },
            false,
        );

        function takePicture(){
            const context = canvas.getContext('2d');
            if(width && height){
                canvas.width = width;
                canvas.height = height;
                context.drawImage(video,0,0,width,height)
                canvas.toBlob(
                    (blob)=>{
                        const file = new File([blob],"capture.png", {type:'image/png'})
                        const dataTransfer = new DataTransfer();
                        dataTransfer.items.add(file);
                        const imagefield = document.getElementById('input-file');
                        imagefield.files = dataTransfer.files;
                    }, "image/png"
                );
            }
            document.querySelector('button[type="submit"]').click();
        }
})();

function checkAndTriggerClick(){
    const imagefield = document.getElementById('input-file');
    if(!imagefield.files.length){
        document.getElementById('click').click();
    }
}

