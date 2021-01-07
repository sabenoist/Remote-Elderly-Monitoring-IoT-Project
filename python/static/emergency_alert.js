   var a = 5;
   if (a>2) {
      popupWin();
      window.onload=popupWin;
   }

   function popupWin() {
      window.open('alert' , 'newWin','width=1000,height=500');
   }