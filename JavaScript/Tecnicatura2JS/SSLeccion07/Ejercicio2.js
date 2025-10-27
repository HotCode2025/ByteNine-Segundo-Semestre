// Ejercicio 2: Crear un sistema simple de gestión de tareas

function createTaskManager() {

    let tasks = [];


    return {

        addTask: function(task) {
            const newTask = {
                id: tasks.length +1,
                nombre: task,
            };
            
            tasks.push(newTask)

        },

        completeTask: function(taskId) {

            const idNum = typeof taskId === "number" ? taskId : Number(taskId);

            const index = tasks.findIndex(t => t.id === idNum);

            if(index !== -1){
                tasks.splice(index, 1);
                console.log("Tarea con ID: "+idNum+" eliminada")
            }else{
                console.log("No se encontro ninguna tarea con el ID: "+taskId);
            }

        },

        listTasks: function() {

            // Tu código aquí
            console.log(tasks);

        }

    };
    
}

// Uso:

const myTasks = createTaskManager();

myTasks.addTask("Aprender JavaScript");

myTasks.addTask("Hacer ejercicio");

myTasks.completeTask(2);

myTasks.listTasks()