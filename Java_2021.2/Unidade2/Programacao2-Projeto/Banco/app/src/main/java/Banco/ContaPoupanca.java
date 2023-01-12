package Banco;

/**
 *
 * @author Gabriel
 */
public class ContaPoupanca extends Conta {

    private int variacao;

    public ContaPoupanca() {
    }

    public ContaPoupanca(int agencia, int num, float saldo, Pessoa dono, int variacao) {
        super(agencia, num, saldo, dono);

        this.variacao = variacao;
    }

    @Override
    public double taxa() {
        return TAXAP;
    }

    public int getVariacao() {
        return variacao;
    }

    public void setVariacao(int variacao) {
        this.variacao = variacao;
    }

    @Override
    public String toString() {
        return """
               ----------------
               |Conta_Poupan�a|
               ----------------
               Usu�rio:\n """ + getDono() + "\nNumero: " + getNum() + "\nSaldo: " + getSaldo() + "\nAgencia: " + getAgencia() + "\nTaxa: " + (getTAXAP() * 100) + "%" + "\nVaria��o: " + this.variacao + "\n";
    }

}