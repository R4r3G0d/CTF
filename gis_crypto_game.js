async function clickElementsWithSameName() {
    const cardElements = document.querySelectorAll('.container .deck .card');

    for (let i = 0; i <= 576; i++) {
        const currentId = i.toString();
        const currentElement = document.getElementById(currentId);

        if (currentElement) {
            const name = currentElement.getAttribute('name');
            currentElement.click();

            await new Promise(resolve => setTimeout(resolve, 0)); // Задержка в 0.5 секунды

            for (const element of cardElements) {
                if (element.getAttribute('name') === name && element.id !== currentId) {
                    element.click();
                    break; // Нажимаем на первый элемент с таким же 'name' и завершаем цикл
                }
            }
        }
    }

    console.log('Все элементы обработаны.');
}

// Вызываем функцию для выполнения операций
clickElementsWithSameName();
