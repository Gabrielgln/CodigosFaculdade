package Medicos;

import java.util.ArrayList;

/**
 *
 * @author Gabriel
 */
public class Lista {

    ArrayList<Medico> listademed;

    public Lista() {
        this.listademed = new ArrayList<>();
    }

    public void insereMed(Medico novoMedico) {
        listademed.add(novoMedico);
    }

    public void listarMed() {
        System.out.println("Lista de m�dicos");

        for (Medico med : listademed) {
            med.listar();
        }
    }

}