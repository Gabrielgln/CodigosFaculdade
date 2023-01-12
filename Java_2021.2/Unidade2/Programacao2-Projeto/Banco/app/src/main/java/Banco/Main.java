package Banco;

import java.util.Scanner;
import javax.swing.JOptionPane;

/**
 *
 * @author Gabriel
 */
public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Lista controle = new Lista();
        int op = 0;
        ContaCorrente cc = new ContaCorrente();
        ContaPoupanca cp = new ContaPoupanca();
        Pessoa p1 = new Pessoa();
        Pessoa p2 = new Pessoa();
        while (op != 6) {
            op = Integer.parseInt(JOptionPane.showInputDialog("COMANDOS:\n"
                    + "1 - Adicionar cliente\n"
                    + "2 - Acessar contas\n"
                    + "3 - Imprimir lista de clientes\n"
                    + "4 - Transferir valores\n"
                    + "5 - Excluir cliente\n"
                    + "6 - Finalizar opera��o"));
            switch (op) {
                case 1:
                    int op2 = Integer.parseInt(JOptionPane.showInputDialog("Digite:\n1 - Adicionar Conta corrente\n2 - Adicionar Conta poupan�a\n3 - Sair"));
                    if (op2 == 1) {
                        p1.setNome((JOptionPane.showInputDialog("Conta Corrente\n"
                                + "Digite seu nome:")));
                        p1.setIdentidade((Integer.parseInt(JOptionPane.showInputDialog("Digite o n�mero da identidade:"))));
                        cc.setAgencia((Integer.parseInt(JOptionPane.showInputDialog("Digite a ag�ncia:"))));
                        cc.setNum((Integer.parseInt(JOptionPane.showInputDialog("Digite o n�mero da conta:"))));
                        cc.setSaldo(Double.parseDouble(JOptionPane.showInputDialog("Digite o saldo:")));
                        cc.setLimite(Double.parseDouble(JOptionPane.showInputDialog("Digite o limite:")));
                        cc.setDono(p1);
                        controle.addConta(cc);
                    } else if (op2 == 2) {
                        p2.setNome((JOptionPane.showInputDialog("Conta Poupan�a\n"
                                + "Digite seu nome:")));
                        p2.setIdentidade((Integer.parseInt(JOptionPane.showInputDialog("Digite o n�mero da identidade:"))));
                        cp.setAgencia((Integer.parseInt(JOptionPane.showInputDialog("Digite a ag�ncia:"))));
                        cp.setNum((Integer.parseInt(JOptionPane.showInputDialog("Digite o n�mero da conta:"))));
                        cp.setSaldo(Double.parseDouble(JOptionPane.showInputDialog("Digite o saldo:")));
                        cp.setVariacao((Integer.parseInt(JOptionPane.showInputDialog("Digite a varia��o:"))));

                        cp.setDono(p2);
                        controle.addConta(cp);
                    } else if (op2 == 3) {
                        JOptionPane.showMessageDialog(null, "Encerrado!");
                    } else {
                        JOptionPane.showMessageDialog(null, "Op��o incorreta!");
                    }
                    break;
                case 2:
                    int op21 = Integer.parseInt(JOptionPane.showInputDialog("Digite:\n1 - Acessar Conta corrente\n2 - Acessar Conta poupan�a\n3 - Sair"));
                    if (op21 == 1) {
                        int op4 = Integer.parseInt(JOptionPane.showInputDialog("Digite:\n1 - Sacar da conta corrente\n2 - Depositar na conta corrente"));
                        if (op4 == 1) {
                            cc.sacar((Double.parseDouble(JOptionPane.showInputDialog("Digite o valor que deseja sacar da conta corrente:"))));
                        } else if (op4 == 2) {
                            cc.depositar((Double.parseDouble(JOptionPane.showInputDialog("Digite o valor que deseja depositar da conta corrente:"))));
                  
                        } else {
                            JOptionPane.showMessageDialog(null, "Op��o incorreta!");
                        }

                    } else if (op21 == 2) {
                        int op4 = Integer.parseInt(JOptionPane.showInputDialog("Digite:\n1 - Sacar da conta poupan�a\n2 - Depositar na conta poupan�a"));
                        if (op4 == 1) {
                            cp.sacar((Double.parseDouble(JOptionPane.showInputDialog("Digite o valor que deseja sacar da conta poupan�a:"))));
                        } else {
                            cp.depositar((Double.parseDouble(JOptionPane.showInputDialog("Digite o valor que deseja depositar da conta poupan�a:"))));
                        }
                    } else if (op21 ==3){
                        JOptionPane.showMessageDialog(null, "Encerrado!");
                    } else{
                        JOptionPane.showMessageDialog(null, "Op��o incorreta!");
                    }

                    break;

                case 3:
                    controle.imprimirClientes();
                    break;
                case 4:
                    int op3 = Integer.parseInt(JOptionPane.showInputDialog("Digite:\n1 - Transferir da conta corrente para conta poupan�a\n2 - Transferir da conta poupan�a para conta corrente\n3 - Sair"));

                    if (op3 == 1) {
                        cc.transferir((Double.parseDouble(JOptionPane.showInputDialog("Digite o valor que deseja transferir:"))), cp);

                    } else if (op3 == 2) {
                        cp.transferir((Double.parseDouble(JOptionPane.showInputDialog("Digite o valor que deseja transferir:"))), cc);
                    } else if (op3 == 3) {
                        JOptionPane.showMessageDialog(null, "Encerrado!");
                    } else {
                        JOptionPane.showMessageDialog(null, "Op��o incorreta!");
                    }
                    break;
                case 5:
                    int op4 = Integer.parseInt(JOptionPane.showInputDialog("Digite o n�mero da conta que deseja excluir:"));
                    controle.excluirCliente(op4);
                    break;

                case 6:
                    JOptionPane.showMessageDialog(null, "Opera��o finalizada!");
                    break;
                default:
                    break;
            }

        }

    }
}