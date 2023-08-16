/*!
* Start Bootstrap - Clean Blog v6.0.9 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if ( currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                console.log(123);
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove(['is-visible']);
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
})


document.addEventListener('DOMContentLoaded', function() {
    // Obtener el botón o enlace de cambio de modo
    const darkModeToggle = document.getElementById('dark-mode-toggle');
  
    // Escuchar el evento de clic en el botón o enlace
    darkModeToggle.addEventListener('click', function() {
      // Cambiar el atributo class del elemento body para alternar entre los modos
      document.body.classList.toggle('dark-mode');
    });
  });


  const avatarInput = document.getElementById('avatar-img-input');
  const avatarPreview = document.getElementById('avatar-preview');
  const noPreview = document.getElementById('no-preview');
  const previewImg = document.getElementById('preview-img');

  avatarInput.addEventListener('change', function() {
    if (this.files && this.files[0]) {
      const reader = new FileReader();
      reader.onload = function(e) {
        previewImg.src = e.target.result;
      };
      reader.readAsDataURL(this.files[0]);
      avatarPreview.style.display = 'block';
      noPreview.style.display = 'none';
    } else {
      avatarPreview.style.display = 'none';
      noPreview.style.display = 'block';
    }
  });