$("body").on("click", ".password-control", function () {
  const passwordInput = $("#password-input");
  const eyeIcon = $(this).find("img"); // Предполагаем, что изображение находится внутри элемента с классом .password-control

  // Если поле с паролем скрыто
  if (passwordInput.attr("type") == "password") {
    $(this).addClass("view");
    passwordInput.attr("type", "text");

    // Изменяем изображение на открытый глазик
    eyeIcon.attr("src", "assets/eye.png");

    // Устанавливаем таймер на 3 секунды
    setTimeout(function () {
      passwordInput.attr("type", "password");
      $(".password-control").removeClass("view");

      // Возвращаем изображение на закрытый глазик
      eyeIcon.attr("src", "assets/eye-hidden.png");
    }, 3000); // 3000 миллисекунд = 3 секунды
  }

  return false;
});
