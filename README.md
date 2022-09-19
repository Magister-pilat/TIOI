# TIOI LR1Подсказка для Docker:
<p>  В папке LR1 присутствуют несколько файлов: generate_and_evaluate.py, my_function.py, Dockerfile и test.py.</p> 
<p>  В файле generate_and_evaluate.py содержатся исходные функции генерации правил и фактов.</p> 
<p>  В файле my_function.py содержатся функции interim_results и results, возвращающие соответственно промежуточные результаты применения правил к фактам без обработки исключения и правила, прошедшие через исключения.</p>
<p>  В файле Dockerfile описана инструкция для Dockerfile, необходимая для построения соответсвующего docker-образа.</p>
<p>  В файле test.py опсан код, необходимый для тестирования и измерния скорости работы функции генерации правил.</p>
<h3>Подсказка для Docker:</h3> 
<p>Для создания Docker-образа необходимо в командной строке прописать следующие команды: </p>
<blockquote> sudo docker build -t name .</blockquote>
