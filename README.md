# Trabajo académico 2 - Topicos de Ciencias de Computación

Problema:<br>
Se requiere que, utilizando como mínimo la ubicación de 10 hospitales, diseñar un CSP que pueda hospedar a 1000+ pacientes de Covid-19. Como restricciones, se pueden definir que:
- Cada hospital tiene una cantidad de camas y no pueden hospedar a más pacientes que esa cantidad
- Los pacientes deben priorizar el hospital más cercano a su ubicación
- Cada paciente tiene un nivel de severidad: A mayor la severidad, mayor la prioridad para ser hospedado en el hospital más cercano.

Modelo Formal:<br>
Conjuntos:<br>
•	𝐻H: Conjunto de hospitales.
•	𝑃P: Conjunto de pacientes.
•	𝐵𝑖Bi: Conjunto de camas en el hospital 𝑖i.

Parámetros:<br>
•	latitud𝑖, longitud𝑖latitudi, longitudi: Coordenadas geográficas del hospital 𝑖i.
•	latitud𝑝, longitud𝑝latitudp, longitudp: Coordenadas geográficas del paciente 𝑝p.
•	severidad𝑝severidadp: Gravedad de la enfermedad del paciente 𝑝p.
•	camas𝑖camasi: Número de camas disponibles en el hospital 𝑖i.

Variables de Decisión:<br>
•	𝑥𝑖𝑗𝑝xijp: Variable binaria que indica si la cama 𝑗j del hospital 𝑖i está asignada al paciente 𝑝p.

Función Objetivo:<br>
  Minimizar∑𝑖∈𝐻∑𝑗∈𝐵𝑖∑𝑝∈𝑃𝑥𝑖𝑗𝑝Minimizar∑i∈H∑j∈Bi∑p∈Pxijp

Restricciones:<br>
1.	Cada paciente 𝑝p debe estar asignado a exactamente una cama en un hospital: ∑𝑖∈𝐻∑𝑗∈𝐵𝑖𝑥𝑖𝑗𝑝=1,∀𝑝∈𝑃∑i∈H∑j∈Bixijp=1,∀p∈P
2.	Cada cama 𝑗j de cada hospital 𝑖i solo puede ser asignada a un paciente 𝑝p: ∑𝑝∈𝑃𝑥𝑖𝑗𝑝≤1,∀𝑖∈𝐻,∀𝑗∈𝐵𝑖∑p∈Pxijp≤1,∀i∈H,∀j∈Bi
3.	Preferencias blandas:
•	Todos los pacientes deben ser asignados a una cama disponible en el hospital más cercano.
•	Los pacientes con mayor severidad deben tener prioridad para ser asignados a camas cuando no haya suficientes disponibles.



Resultados:<br>



Conclusiones:<br>
- La programación de restricciones es esencial para modelar eficazmente la asignación de pacientes a hospitales durante una pandemia.
- Es crucial diferenciar entre restricciones duras (esenciales) y blandas (preferencias) para garantizar la viabilidad y satisfacción del modelo.
- La utilización de datos reales, como coordenadas geográficas, es fundamental para diseñar un modelo realista y efectivo.
- El modelo debe ser flexible y adaptable para enfrentar diferentes escenarios durante una crisis de salud.
- La presentación clara de resultados, incluidos mapas y análisis visuales, es crucial para comunicar conclusiones y recomendaciones a las partes interesadas.
