//Desenvolvido por Geraldo Junior
//Harpia Aerodesign - Cargas e Aeroelasticidade 2020

#include<stdio.h>
#include<stdlib.h>
#include <sstream>
#include<math.h>
#include<fstream>
#include <iostream>

using namespace std;

double atiradordeeleite = 0;
double arquivo2 = 0;
int cp1=0;
int cp2=0;

void desempenho(double entrada);
void vn(double W, double vmax, double S, double cl, double ro, double Sref);
void EVeEH(double n1, double WSm, double WSmin, double Vasel, double Vamin, double Vcsel, double Vcmin);
void profundor(double supcarga, double condapontaEH, double cordaraizEH, double envergaduraEH);
void cacetinhodearrasto(double supcarga, double condapontaEV, double condaraizEV, double envergaduraEV);
void calculaemp2(double f, double fac, double m1, double m2, double m3, double supcarga, double condapontaEH, double hingeponta, double cordaponta, double envergadura, int jacare);
void junqueira(double n1, double WSm, double WSmin, double Vasel, double Vamin, double Vcsel, double Vcmin);
void aileron1(double fc, double aileron);
void TAB1(double fc, double TAB);
void FLAP1(double fc, double FLAP);
void supasa(double evnergadura, double area, double carga, double envergadura, double cordaraiz, double cordaponta, double hingeraiz, double hingeponta);
void TABFLAP(double f, double fac, double m1, double m2, double carga, double hingeponta, double cordaponta, double envergadura, double area);
void calculaemp1(double f, double fac, double m1, double m2, double carga, double hingeponta, double cordaponta, double envergadura, double area);
void FLAPTAB(double f, double fac, double m1, double m2, double carga, double hingeponta, double cordaponta, double envergadura, double area);
void cetinho(double f, double fac, double m1, double m2, double m3, double supcarga, double condapontaEH, double hingeponta, double cordaponta, double envergadura, int jacare);
void cpprofundor(double car);
void cpcacetinho(double car);
double cpaolongodoperfil (double espessura, double distancia, double comprimento,double cp, double ro, double velocidadeAnalise);
void cp(double ro, double vmax);
void tremdepouso(double W, double A, double Cl, double Ca);
void limpa1(double car);
void limpa2(double car);


int main(){

    double n;
    limpa1(n);
    limpa2(n);

	desempenho(1);

	//cout << "\n" << "\n" << "\n" << "\n" << "digite uma letra ou numero para sair: " << "\n";
    //cin >> n;

	return 0;
}

void desempenho(double tico){

	ifstream dados_aerodinamicos;
    double access[20];
	string linha;

	dados_aerodinamicos.open("dados_aerodinamicos.txt");

    for(int p=0; p<21; p++){
        getline(dados_aerodinamicos,linha);
        stringstream alicate(linha);
        alicate >> access[p];
    }

    double ro950;
    double ro0 = 1.225;
    double entrada = access[0];
    double h=access[1];
    double envergadura = access[2];
	double S = access[3];
	double AR=(pow(envergadura,2)/S);

	double K0= access[4];
	double K1= access[5];
	double K2= access[6];
	double Cl0= access[7];
	double Cl0iw = access[8];
	double cl = access[9]; //cl do menino

	double mi = access[10]; //atrito da roda
	double tdapista= entrada; //tamanho da pista
	double incmotor= access[11]; //inclinação do motor
	incmotor = incmotor*0.0174533;
	double alturadaasa = access[12]; //Altura da asa
	double peso = access[18]; //massa
    double distancia;
    double j;
    double a0=access[13];
	double a=access[14]; // v^3
	double b=access[15];   // v^2
	double c= access[16];   // v^1
	double d=access[17];        // v^0
    double W;
    double ro=access[19];
    double Sref=access[20];
    double vmax = 0;
    double v = 10;

	while (v<45){
        W = peso*9.81;
		double Tracao=a0*(pow(v,4))+a*(pow(v,3))+b*(pow(v,2))+(c*v)+d;

		double Trequerido=0.5*ro*(S/2)*K0*(pow(v,2))+ K1*W+ (2*K2*(pow(W,2)))/(ro*(S/2)*(pow(v,2)));
		double Tdisponivel = Tracao*(ro/ro0);

        double tulio = Tdisponivel - Trequerido;

        if (tulio < 0.04 && tulio > 0){
            //cout << "A velocidade maxima e:" << " " << v << " " << "m/s" << endl;
            vmax = v;


        }

		v = v + 0.01;
	}
	ifstream dados_analise;
    double morp[7];
	string linhaa;

	dados_analise.open("dados_analise.txt");

    for(int p=0; p<7; p++){
        getline(dados_analise,linhaa);
        stringstream alicate(linhaa);
        alicate >> morp[p];
    }
    W=morp[2];
    W = W*9.81;

    tremdepouso(W, S, cl, mi);
	vn(W,vmax,S, cl, ro, Sref);
	cp(ro,vmax);

}

void tremdepouso(double W, double A, double Cl, double Ca){

    ifstream dados_tremdepouso;
    double access[5];
	string linha;

	dados_tremdepouso.open("dados_tremdepouso.txt");

    for(int p=0; p<5; p++){
        getline(dados_tremdepouso,linha);
        stringstream alicate(linha);
        alicate >> access[p];
    }

	double T = access[0]; //angulo de tipback
	double H = access[1]; // altura do CG
	double P = access[2]; // proporção de peso
	double O = access[3]; //angulo de turnover
    double Fs = access[4];

    ofstream output_tremdepouso;
	output_tremdepouso.open("output_tremdepouso.txt");

	double D1 = tan(O)*H;
	double D  = D1/P;
	double D2 = D-D1;
	double F = 2*(tan(asin((H/tan(O*(3.14/180)))/D2)))*D;

	output_tremdepouso << "CG -> TPP: "  <<  D1 <<endl;
	output_tremdepouso << "TTP -> triquilha: "  << D<<endl;
	output_tremdepouso << "CG -> triquilha: " <<  D2<<endl;
	output_tremdepouso << "Entre rodas: " <<  F << "\n" <<endl;

	double L = Cl*0.66; //canoli de pouso
	double Vv = 0.55*(pow((W*A),0.25));
	double Aq = 0.0132*sqrt(A/L);
	double Fi = 2.5+(L/W); //caloni inercial
	double k = 0.25; //fator k
	double Cv = (Fi-L)*W*(D1/D)*Fs;
	double Ch = k*Fi*W*(D1/D)*Fs;
	double Cv1= (Fi-L)*W*(D2/D)*Fs;
	double Ch1= k*Fi*W*(D2/D)*Fs;
	double Fli= W*0.5*Fs;
	double Fle= W*0.33*Fs;
	double Cv2= (Fi-L)*W*Fs;
	double Ch2= 0.25*Fi*W*Fs;
	double Fli1=W*Fs*0.5;
	double Fle2=W*Fs*0.33;
	double Cv3= W*Fs*1.33;
	double Ch3= Ca*Cv3*Fs;

	output_tremdepouso << "DropTest " << "\n" << endl;
	output_tremdepouso << "velocidade (m/s): " <<  Vv << endl;
	output_tremdepouso << "altura (m): "  << Aq << "\n" << endl;

	output_tremdepouso << "Situação de pouso em 3 rodas: " << "\n" << endl;

	output_tremdepouso << "Triquilha: " << endl;
	output_tremdepouso << "Componente Vertical (N): "  << Cv << endl;
	output_tremdepouso << "Componente Horizontal (N): "  << Ch << "\n" << endl;

	output_tremdepouso << "Trem de pouso principal: " << endl;
	output_tremdepouso << "Componente Vertical (N): "  << Cv1 << endl;
	output_tremdepouso << "Componente horizontal (N): "  << Ch1 << endl;
	output_tremdepouso << "força lateral interna (N): "  << Fli << endl;
	output_tremdepouso << "força lateral externa (N): "  << Fle << "\n" << endl;

	output_tremdepouso << "Situação de pouso em 2 rodas: " << "\n" << endl;
	output_tremdepouso << "Trem de pouso principal: " << endl;
	output_tremdepouso << "Componente Vertical (N): "  << Cv2 << endl;
	output_tremdepouso << "Componente Horizontal (N): "  << Ch2 << endl;
	output_tremdepouso << "força lateral interna (N): "  << Fli1 << endl;
	output_tremdepouso << "força lateral externa (N): "  << Fle2 << "\n" << endl;

	output_tremdepouso << "Situação de pouso em 1 roda: "  << "\n" << endl;
	output_tremdepouso << "Trem de pouso principal: " << endl;
	output_tremdepouso << "Componente Vertical (N): " << Cv3 << endl;
	output_tremdepouso << "Componente Horizontal (N): "<< Ch3 << endl;

	output_tremdepouso.close();
}


void vn(double W, double vmax, double S, double cl, double ro, double Sref){

    ofstream output_vn;
    ofstream output_vnmsm;
	ofstream output_vnmin;
	output_vn.open("output_vn.txt");
	output_vnmsm.open("output_vnmsm.txt");
	output_vnmin.open("output_vnmin.txt");

	// calculo do diagrama vn

	ifstream dados_analise;
    double morp[7];
	string linha;

	dados_analise.open("dados_analise.txt");

    for(int p=0; p<7; p++){
        getline(dados_analise,linha);
        stringstream alicate(linha);
        alicate >> morp[p];
    }

    W = (W*2.20462)/9.81;
    S = S*10.7639;
    ro = ro*0.062428;
    double n1 = morp[0];
    double n2 = morp[1];
    double Wmin = morp[2];
    double clalpha = morp[3];
    double cmedia = morp[4];
    cmedia = cmedia*3.28084;
    double rajada1 = morp[5];
    rajada1 = 1.94384*rajada1;
    double rajada2 = morp[6];
    rajada2 = 1.94384*rajada2;
	double WSm = W/S;
	double WSmin = Wmin/S;
	WSmin = WSmin*2.20462;
	double n3, n3m;// FCr+
	double n4, n4m; // FCr-
	double Vfmin = 11*sqrt(n1*WSm); //vminima
	double Vamin = 15*sqrt(n1*WSm); //velocidade mínima de manobra
	double Vcmin = 17*sqrt(n1*WSm); //velocidade mínima de cruzeiro
	double Vdmin = 24*sqrt(n1*WSm); //velocidade mínima de mergulho

    ofstream output_vels;
	output_vels.open("output_vels.txt");
	//output_tremdepouso << "velocidade: " <<  Vv << endl;
	//output_tremdepouso << "altura: "  << Aq << "\n" << endl;
	//output_tremdepouso.close();

	double Vfsel = sqrt((2*(9.81*W/2.20462)*1)/((ro/0.062428)*(Sref)*cl)); //velocidade de stall90
    //cout << "A velocidade de stall e:" << " " << Vfsel << " " << "m/s" << endl;
    output_vels << "A velocidade de stall e:" << " " << Vfsel << " " << "m/s" << endl;
	Vfsel = Vfsel*1.94384;

    double Vcsel = 0.9*vmax; //velocidade de cruzeiro160
	//cout << "A velocidade de cruzeiro e:" << " " << Vcsel << " " << "m/s" << endl;
	output_vels << "A velocidade de cruzeiro e:" << " " << Vcsel << " " << "m/s" << endl;
	Vcsel = Vcsel*1.94384;

	double Vasel = (Vfsel/1.94384*(sqrt(n1))); //velocidade de manobra120
	//cout << "A velocidade de manobra e:" << " " << Vasel << " " << "m/s" << endl;
	output_vels << "A velocidade de manobra e:" << " " << Vasel << " " << "m/s" << endl;
	Vasel = Vasel*1.94384;

	double Vdsel = 1.25*vmax; //velocidade de mergulho190
	//cout << "A velocidade de mergulho e:" << " " << Vdsel << " " << "m/s" << "\n" "\n" << endl;
	output_vels << "A velocidade de mergulho e:" << " " << Vdsel << " " << "m/s" << "\n" "\n" << endl;
	Vdsel = Vdsel*1.94384;

	double K = Vcsel/Vcmin;
	double canoli1, canoli2, canoli3, canoli4;
	double humberto, hdoisberto, htresberto, hquatroberto, hcincoberto,  hseisberto;
    double olho1 = n1*WSm;
	double olho2 = n1*WSmin;

	double mi = (2*((WSm*S)/(Sref*2*10.7639)))/(ro*cmedia*clalpha);

    output_vels.close();
	//determinação do coeficiente n3

	if (K>1.5){
		n3 = 1.5;
	}

	if (K<1.5 && K>1.4){
		canoli1 = 2.6889;
		canoli2 = -0.21;
		canoli3 = 2.51;
		canoli4= -0.209;
		humberto =  canoli1*(pow(olho1,canoli2));
		hdoisberto = canoli3*(pow(olho1,canoli4));
		htresberto = ((humberto - hdoisberto)/(1.5-1.4))*(K-1.4)+hdoisberto;
		hquatroberto = canoli1*(pow(olho2,canoli2));
		hcincoberto =  canoli3*(pow(olho2,canoli4));
		hseisberto = ((hquatroberto - hcincoberto)/(1.5-1.4))*(K-1.4)+hcincoberto;
		n3 = htresberto*n1;
		n3m = hseisberto*n1;

	}

	if (K<1.4 && K>1.3){
		canoli1 = 2.51;
		canoli2 = -0.209;
		canoli3 = 2.38;
		canoli4 = -0.209;
		humberto =  canoli1*(pow(olho1,canoli2));
		hdoisberto = canoli3*(pow(olho1,canoli4));
		htresberto = ((humberto - hdoisberto)/(1.4-1.3))*(K-1.3)+hdoisberto;
		hquatroberto = canoli1*(pow(olho2,canoli2));
		hcincoberto =  canoli3*(pow(olho2,canoli4));
		hseisberto = ((hquatroberto - hcincoberto)/(1.4-1.3))*(K-1.3)+hcincoberto;
		n3 = htresberto*n1;
		n3m = hseisberto*n1;
	}

	if (K<1.3 && K>1.2){
		canoli1 = 2.38;
		canoli2 = -0.209;
		canoli3 = 2.21;
		canoli4= -0.209;
		humberto =  canoli1*(pow(olho1,canoli2));
		hdoisberto = canoli3*(pow(olho1,canoli4));
		htresberto = ((humberto - hdoisberto)/(1.3-1.2))*(K-1.2)+hdoisberto;
		hquatroberto = canoli1*(pow(olho2,canoli2));
		hcincoberto =  canoli3*(pow(olho2,canoli4));
		hseisberto = ((hquatroberto - hcincoberto)/(1.3-1.2))*(K-1.2)+hcincoberto;
		n3 = htresberto*n1;
		n3m = hseisberto*n1;
	}

	if (K<1.2 && K>1.1){
		canoli1 = 2.21;
		canoli2 = -0.209;
		canoli3 = 2.08;
		canoli4= -0.209;
		humberto =  canoli1*(pow(olho1,canoli2));
		hdoisberto = canoli3*(pow(olho1,canoli4));
		htresberto = ((humberto - hdoisberto)/(1.2-1.1))*(K-1.1)+hdoisberto;
		hquatroberto = canoli1*(pow(olho2,canoli2));
		hcincoberto =  canoli3*(pow(olho2,canoli4));
		hseisberto = ((hquatroberto - hcincoberto)/(1.2-1.1))*(K-1.1)+hcincoberto;
		n3 = htresberto*n1;
		n3m = hseisberto*n1;
	}

	if (K<1.1){
		canoli1 = 2.08;
		canoli2 = -0.209;
		canoli3 = 1.92;
		canoli4= -0.209;
		humberto =  canoli1*(pow(olho1,canoli2));
		hdoisberto = canoli3*(pow(olho1,canoli4));
		htresberto = (( humberto - hdoisberto)/(1.1-1.0))*(K-1.0)+hdoisberto;
		hquatroberto = canoli1*(pow(olho2,canoli2));
		hcincoberto =  canoli3*(pow(olho2,canoli4));
		hseisberto = ((hquatroberto - hcincoberto)/(1.1-1.0))*(K-1.0)+hcincoberto;
		n3 = htresberto*n1;
		n3m = hseisberto*n1;
	}
	double n3cvn = 1+((ro/0.062428)*(Vcsel/1.94384)*clalpha*((0.88*mi)/(5.3+mi))*(rajada2/1.94384))/(2*W*(9.81/2.20462)/(Sref*2));
	double n3dvn = 1+((ro/0.062428)*(Vdsel/1.94384)*clalpha*((0.88*mi)/(5.3+mi))*(rajada1/1.94384))/(2*W*(9.81/2.20462)/(Sref*2));
	//determinação do coeficiente n4



	if (K<1.5 && K>1.4){
		canoli1 = 2.3;
		canoli2 = -0.32;
		canoli3 = 2.1;
		canoli4= -0.32;
		humberto =  canoli1*(pow(olho1,canoli2));
		hdoisberto = canoli3*(pow(olho1,canoli4));
		htresberto = ((humberto - hdoisberto)/(1.5-1.4))*(K-1.4)+hdoisberto;
		hquatroberto = canoli1*(pow(olho2,canoli2));
		hcincoberto =  canoli3*(pow(olho2,canoli4));
		hseisberto = ((hquatroberto - hcincoberto)/(1.5-1.4))*(K-1.4)+hcincoberto;
		n4 = -htresberto*n1;
		n4m = -hseisberto*n1;

	}

	if (K<1.4 && K>1.3){
		canoli1 = 2.1;
		canoli2 = -0.32;
		canoli3 = 1.9;
		canoli4= -0.32;
		humberto =  canoli1*(pow(olho1,canoli2));
		hdoisberto = canoli3*(pow(olho1,canoli4));
		htresberto = ((humberto - hdoisberto)/(1.4-1.3))*(K-1.3)+hdoisberto;
		hquatroberto = canoli1*(pow(olho2,canoli2));
		hcincoberto =  canoli3*(pow(olho2,canoli4));
		hseisberto = ((hquatroberto - hcincoberto)/(1.4-1.3))*(K-1.3)+hcincoberto;
		n4 = -htresberto*n1;
		n4m = -hseisberto*n1;
	}

	if (K<1.3 && K>1.2){
		canoli1 = 1.9;
		canoli2 = -0.32;
		canoli3 = 1.72;
		canoli4= -0.32;
		humberto =  canoli1*(pow(olho1,canoli2));
		hdoisberto = canoli3*(pow(olho1,canoli4));
		htresberto = ((humberto - hdoisberto)/(1.3-1.2))*(K-1.2)+hdoisberto;
		hquatroberto = canoli1*(pow(olho2,canoli2));
		hcincoberto =  canoli3*(pow(olho2,canoli4));
		hseisberto = ((hquatroberto - hcincoberto)/(1.3-1.2))*(K-1.2)+hcincoberto;
		n4 = -htresberto*n1;
		n4m = -hseisberto*n1;
	}

	if (K<1.2 && K>1.1){
		canoli1 = 1.72;
		canoli2 = -0.32;
		canoli3 = 1.53;
		canoli4= -0.32;
		humberto =  canoli1*(pow(olho1,canoli2));
		hdoisberto = canoli3*(pow(olho1,canoli4));
		htresberto = ((humberto - hdoisberto)/(1.2-1.1))*(K-1.1)+hdoisberto;
		hquatroberto = canoli1*(pow(olho2,canoli2));
		hcincoberto =  canoli3*(pow(olho2,canoli4));
		hseisberto = ((hquatroberto - hcincoberto)/(1.2-1.1))*(K-1.1)+hcincoberto;
		n4 = -htresberto*n1;
		n4m = -hseisberto*n1;
	}

	if (K<1.1){
		canoli1 = 1.53;
		canoli2 = -0.32;
		canoli3 = 1.34;
		canoli4= -0.32;
		humberto =  canoli1*(pow(olho1,canoli2));
		hdoisberto = canoli3*(pow(olho1,canoli4));
		htresberto = (( humberto - hdoisberto)/(1.1-1.0))*(K-1.0)+hdoisberto;
		hquatroberto = canoli1*(pow(olho2,canoli2));
		hcincoberto =  canoli3*(pow(olho2,canoli4));
		hseisberto = ((hquatroberto - hcincoberto)/(1.1-1.0))*(K-1.0)+hcincoberto;
		n4 = -htresberto*n1;
		n4m = -hseisberto*n1;


	}
	double n4cvn = 1-((ro/0.062428)*(Vcsel/1.94384)*clalpha*((0.88*mi)/(5.3+mi))*(rajada2/1.94384))/(2*W*(9.81/2.20462)/(Sref*2));
	double n4dvn = 1-((ro/0.062428)*(Vdsel/1.94384)*clalpha*((0.88*mi)/(5.3+mi))*(rajada1/1.94384))/(2*W*(9.81/2.20462)/(Sref*2));

	//diagrama vn para MTOW

	double va1 = Vasel;
	double na1 = n1;
	double k = 0;
	double juaoma;

	while (na1>0.001){
		na1 = na1/(1+k);
		juaoma = ((pow(na1,(0.5)))*va1)/(pow(n1,(0.5)));

		output_vn << juaoma*0.514444 << "    " << na1 << "\n";

		if(K<2){
			k=k+0.1;
		}
	}

	double va2 = Vasel;
	double na2 = n2;
	k = 0;
    double juao;
	double arbusto0 = (W*na2)/(pow((0.00237*-1.35*na2),(0.5)));
    double arbusto;
	while (na2<-0.001){
		na2 = na2/(1+k);
		arbusto = (W*na2)/(pow((0.00237*-1.35*na2),(0.5)));
		juao = va2*arbusto/arbusto0;

		output_vn << juao*0.514444 << "    " << na2 << "\n";

		if(K<2){
			k=k+0.1;
		}
	}

	output_vn << Vasel*0.514444 << "    " << n1 << "\n";
	output_vn << Vcsel*0.514444 << "    " << n3 << "\n";
	output_vn << Vdsel*0.514444 << "    " << n1 << "\n";
	output_vn << Vdsel*0.514444 << "    " << n2 << "\n";
	output_vn << Vcsel*0.514444 << "    " << n4 << "\n";
	output_vn << Vasel*0.514444 << "    " <<  n2 << "\n";

	output_vn << "0" << "           " << "1" << "\n";
	output_vn << Vasel*0.514444 << "    " << n1 << "\n";
	output_vn << Vasel*0.514444 << "    " << n2 << "\n";
    output_vn << "0" << "           " << "1" << "\n";
	output_vn << Vdsel*0.514444 << "    " << n1 << "\n";
	output_vn << Vdsel*0.514444 << "    " << n2 << "\n";
	output_vn << Vasel*0.514444 << "    " << n2 << "\n";
	output_vn << Vdsel*0.514444 << "    " << n2 << "\n";
	output_vn << Vasel*0.514444 << "    " << n1 << "\n";
	output_vn << Vdsel*0.514444 << "    " << n1 << "\n";
	output_vn << Vdsel*0.514444 << "    " << n1 << "\n";
	output_vn << Vdsel*0.514444 << "    " << n2 << "\n";

	//diagrama vn mesmo

    va1 = Vasel;
	na1 = n1;
	k = 0;
	juaoma;

	while (na1>0.001){
		na1 = na1/(1+k);
		juaoma = ((pow(na1,(0.5)))*va1)/(pow(n1,(0.5)));

		output_vnmsm << juaoma*0.514444 << "    " << na1 << "\n";

		if(K<2){
			k=k+0.1;
		}
	}

	va2 = Vfsel;
	na2 = n2;
	k = 0;
    juao;
	arbusto0 = (W*na2)/(pow((0.00237*-1.35*na2),(0.5)));
    arbusto;
	while (na2<-0.001){
		na2 = na2/(1+k);
		arbusto = (W*na2)/(pow((0.00237*-1.35*na2),(0.5)));
		juao = va2*arbusto/arbusto0;

		output_vnmsm << juao*0.514444 << "    " << na2 << "\n";

		if(K<2){
			k=k+0.1;
		}
	}

    output_vnmsm << Vasel*0.514444 << "    " << n1 << "\n";
	output_vnmsm << Vcsel*0.514444 << "    " << n3cvn << "\n";
	output_vnmsm << Vdsel*0.514444 << "    " << n1 << "\n";
	output_vnmsm << Vdsel*0.514444 << "    " << n2 << "\n";
	output_vnmsm << Vdsel*0.514444 << "    " << n4dvn << "\n";
	output_vnmsm << Vfsel*0.514444 << "    " <<  n2 << "\n";

	output_vnmsm << "0" << "           " << "1" << "\n";
	output_vnmsm << Vcsel*0.514444 << "    " << n3cvn << "\n";
	output_vnmsm << Vcsel*0.514444 << "    " << n4cvn << "\n";
    output_vnmsm << "0" << "           " << "1" << "\n";
	output_vnmsm << Vdsel*0.514444 << "    " << n3dvn << "\n";
	output_vnmsm << Vdsel*0.514444 << "    " << n4dvn << "\n";
	output_vnmsm << Vfsel*0.514444 << "    " << n2 << "\n";
	output_vnmsm << Vdsel*0.514444 << "    " << n2 << "\n";
	output_vnmsm << Vasel*0.514444 << "    " << n1 << "\n";
	output_vnmsm << Vdsel*0.514444 << "    " << n1 << "\n";
	output_vnmsm << Vdsel*0.514444 << "    " << n1 << "\n";
	output_vnmsm << Vdsel*0.514444 << "    " << n2 << "\n";


	//diagrama vn para TOWmin

	va1 = Vasel; //vamin ou vasel?????????????????
	na1 = n1;
    k = 0;
	juaoma;
	while (na1>0.001){
		na1 = na1/(1+k);
		juaoma = (pow(na1,(0.5))*va1)/pow(n1,(0.5));
		output_vnmin << juaoma*0.514444 << "    " << na1 << "\n";
			if(K<2){
				k=k+0.1;
			}
	}
	va2 = Vasel; //vamin ou vasel?????????????????
	na2 = n2;
	k = 0;
	arbusto0 = (W*na2)/(pow((0.00237*-1.35*na2),(0.5)));

	while (na2<-0.001){
		na2 = na2/(1+k);
		arbusto = (W*na2)/(pow((0.00237*-1.35*na2),(0.5)));
		juao = va2*arbusto/arbusto0;
		output_vnmin << juao*0.514444 << "    " << na2 << "\n";
			if(K<2){
				k=k+0.1;
			}

	}

	output_vnmin << Vasel*0.514444 << "    " << n1 << "\n";
	output_vnmin << Vcmin*0.514444 << "    " << n3m << "\n";
	output_vnmin << Vdmin*0.514444 << "    " << n1 << "\n";
	output_vnmin << Vdmin*0.514444 << "    " << n2 << "\n";
	output_vnmin << Vcmin*0.514444 << "    " << n4m << "\n";
	output_vnmin << Vfmin*0.514444 << "    " <<  n2 << "\n";

	output_vnmin << "0" << "            " << "1" << "\n";
	output_vnmin << Vamin*0.514444 << "    " << n1 << "\n";
	output_vnmin << Vamin*0.514444 << "    " << n2 << "\n";
    output_vnmin << "0" << "            " << "1" << "\n";
	output_vnmin << Vdmin*0.514444 << "    " << n1 << "\n";
	output_vnmin << Vdmin*0.514444 << "    " << n2 << "\n";
	output_vnmin << Vamin*0.514444 << "    " << n2 << "\n";
	output_vnmin << Vdmin*0.514444 << "    " << n2 << "\n";
	output_vnmin << Vasel*0.514444 << "    " << n1 << "\n";
	output_vnmin << Vdmin*0.514444 << "    " << n1 << "\n";
	output_vnmin << Vdmin*0.514444 << "    " << n1 << "\n";
	output_vnmin << Vdmin*0.514444 << "    " << n2 << "\n";

	EVeEH(n1, WSm, WSmin, Vasel, Vamin, Vcsel, Vcmin);
	junqueira(n1, WSm, WSmin, Vasel, Vamin, Vcsel, Vcmin);

	output_vn.close();
	output_vnmin.close();
	output_vnmsm.close();
}

void EVeEH(double n1, double WSm, double WSmin, double Vasel, double Vamin, double Vcsel, double Vcmin){

	//calculo de cargas no EH e EV

    ifstream i_EH;
    ifstream i_EV;
	double cordapontaEH, cordaraizEH, envergaduraEH, cordapontaEV, cordaraizEV, envergaduraEV;
	string linha;

    i_EH.open("i_EH.txt");

    getline(i_EH,linha);
    stringstream geek(linha);
    geek >> cordapontaEH;

	getline(i_EH,linha);
    stringstream geek2(linha);
    geek2 >> cordaraizEH;

	getline(i_EH,linha);
    stringstream geek3(linha);
    geek3 >> envergaduraEH;

    i_EV.open("i_EV.txt");

	getline(i_EV,linha);
    stringstream geek4(linha);
    geek4 >> cordapontaEV;

	getline(i_EV,linha);
    stringstream geek5(linha);
    geek5 >> cordaraizEV;

    getline(i_EV,linha);
    stringstream geek6(linha);
    geek6 >> envergaduraEV;

    cordapontaEH = cordapontaEH*3.28084;
    cordaraizEH =  cordaraizEH*3.28084;
	envergaduraEH = envergaduraEH*3.28084;

	cordapontaEV =  cordapontaEV*3.28084;
	cordaraizEV =  cordaraizEV*3.28084;
	envergaduraEV =  envergaduraEV*3.28084;

    double areaEH = envergaduraEH*(cordapontaEH+cordaraizEH)/2;
    double areaEV = envergaduraEV*(cordapontaEV+cordaraizEV)/2;

	double olho1 = n1*WSm;
	double olho2 = n1*WSmin;
	double EV;
	double EH;

	if(olho1<47){
		EV = 3.66*pow(olho1,0.5);
	}
	else{
		EV = 0.534*olho1;
	}

	EH = 4.8+0.534*olho1;

	double fc;
	double fc1 = pow((Vasel/Vamin),2);
	double fc2 = pow((Vcsel/Vcmin),2);

	if(fc1>fc2){
		fc = fc1;
	}
	else{
		fc = fc2;
	}

	EH = EH*fc;
	EV = EV*fc;

	profundor(EH, cordapontaEH, cordaraizEH, envergaduraEH);
	cacetinhodearrasto(EV, cordapontaEV, cordaraizEV, envergaduraEV);

    EH = EH*areaEH;
    EV = EV*areaEV;

    ofstream output_EVEH;
	output_EVEH.open("output_EVEH.txt");

	//cout << "carregamento no EV :" << " " << EV*4.4452 << " " << "N" << endl ;
    //cout << "carregamento no EH :" << " " << EH*4.4452 << " " << "N" << "\n" << "\n" ;
    output_EVEH << "carregamento no EV :" << " " << EV*4.4452 << " " << "N" << endl ;
    output_EVEH << "carregamento no EH :" << " " << EH*4.4452 << " " << "N" << "\n" << "\n" ;

    output_EVEH.close();

}

void profundor(double supcarga, double condapontaEH, double cordaraizEH, double envergaduraEH){

	//calculo de carga no pofundor

    ifstream i_profundor;
	double cordaponta, cordaraiz, hingeponta, hingeraiz, envergadura;
	string linha;
    i_profundor.open("i_profundor.txt");
    getline(i_profundor,linha);
    stringstream geek(linha);
    geek >> cordaponta;
	getline(i_profundor,linha);
    stringstream geek2(linha);
    geek2 >> cordaraiz;
	getline(i_profundor,linha);
    stringstream geek3(linha);
    geek3 >> hingeponta;
	getline(i_profundor,linha);
    stringstream geek4(linha);
    geek4 >> hingeraiz;
	getline(i_profundor,linha);
    stringstream geek5(linha);
    geek5 >> envergadura;


    cordaponta = cordaponta*3.28084;
    cordaraiz =  cordaraiz*3.28084;
	hingeponta = hingeponta*3.28084;
	hingeraiz =  hingeraiz*3.28084;
	envergadura =  envergadura*3.28084;

    double area = envergadura*(cordaponta + cordaraiz)/2;
	double f = envergadura/30;
	double fac = area*envergadura;
	double m1 = (cordaraiz-cordaponta)/envergadura;
	double m2 = (hingeraiz - hingeponta)/envergadura;
	double m3 = (cordaraizEH - condapontaEH)/envergaduraEH;

    ofstream output_pro;
	output_pro.open("output_pro.txt");

    //cout << "carregamento total no profundor:" << "  " << area*supcarga*4.4452 << " " << "N" << endl;
    output_pro << "carregamento total no profundor:" << "  " << area*supcarga*4.4452 << " " << "N" << endl;

    output_pro.close();


	calculaemp2(f, fac, m1, m2, m3, supcarga, condapontaEH, hingeponta, cordaponta, envergadura, 1);


}

void cacetinhodearrasto(double supcarga, double condapontaEV, double condaraizEV, double envergaduraEV){

    ifstream i_cacetinhodearrasto;
	double cordaponta, cordaraiz, hingeponta, hingeraiz, envergadura;
	string linha;
    i_cacetinhodearrasto.open("i_cacetinhodearrasto.txt");
    getline(i_cacetinhodearrasto,linha);
    stringstream geek(linha);
    geek >> cordaponta;
	getline(i_cacetinhodearrasto,linha);
    stringstream geek2(linha);
    geek2 >> cordaraiz;
	getline(i_cacetinhodearrasto,linha);
    stringstream geek3(linha);
    geek3 >> hingeponta;
	getline(i_cacetinhodearrasto,linha);
    stringstream geek4(linha);
    geek4 >> hingeraiz;
	getline(i_cacetinhodearrasto,linha);
    stringstream geek5(linha);
    geek5 >> envergadura;

    cordaponta = cordaponta*3.28084;
    cordaraiz =  cordaraiz*3.28084;
	hingeponta = hingeponta*3.28084;
	hingeraiz =  hingeraiz*3.28084;
	envergadura =  envergadura*3.28084;

    double area = envergadura*(cordaponta + cordaraiz)/2;
	double f = envergadura/30;
	double fac = area*envergadura;
	double m1 = (cordaraiz-cordaponta)/envergadura;
	double m2 = (hingeraiz - hingeponta)/envergadura;
	double m3 = (condaraizEV - condapontaEV)/envergaduraEV;


    ofstream output_tin;
	output_tin.open("output_tin.txt");

	//cout << "carregamento total no cetinho de arrasto:" << "  " << area*supcarga*4.4452 << " " << "N" << "\n" << "\n";
    output_tin << "carregamento total no cetinho de arrasto:" << "  " << area*supcarga*4.4452 << " " << "N" << "\n" << "\n";

    output_tin.close();
	cetinho(f, fac, m1, m2, m3, supcarga, condapontaEV, hingeponta, cordaponta, envergadura, 2);


}

void calculaemp2(double f, double fac, double m1, double m2, double m3, double supcarga, double condapontaEH, double hingeponta, double cordaponta, double envergadura, int jacare){

    ofstream output_profundor;
    output_profundor.open("output_profundor.txt");

	//calculo de sustentação ao longo da envergadura

	double i = 0;
	double CARGAAA = 0;
	double MOMENTOO = 0;
	double x = 0;
	double car = 0;
	double car2 =0;
	double tinho = f;
    double sominha = 0;
    double somona = 0;

	while (f<(envergadura+0.1)){
		//double croc = envergadura -
		//double crocm = -1*croc;
		double midi = (i+f)/2;
		double a1 = midi*m1 + cordaponta;
		double a2 = midi*m2 + hingeponta;
		double a3 = midi*m3 + condapontaEH;
		double j = 0.95;
		double range = 0.1;
		double e = a1/10;
		double ih = a1 - a2;
		double trucao;
		double arco;
        sominha = 0;
        somona = 0;
		arco = 0;
		while(j>(0.0)){
			x = a3-(a3-j*a1);
			trucao = 3*supcarga*(pow(((a3-(a3-j*a1))/a1),2));
			car = trucao*(e*tinho);
			car2 = trucao*(e*f);
			sominha = sominha + car2;
			arco = car*(x-ih);
			somona = somona + arco;
			j = j-range;
			cpprofundor(car);

		}

		CARGAAA = sominha/f;
		MOMENTOO = somona;

        output_profundor << i*0.3048 << "    " << CARGAAA*14.584 << "    " << MOMENTOO*4.4452 <<  "\n";

		i = f;
		f = tinho + f;
	}
    output_profundor.close();


}

void cetinho(double f, double fac, double m1, double m2, double m3, double supcarga, double condapontaEH, double hingeponta, double cordaponta, double envergadura, int jacare){

    ofstream output_cacetinhodearrasto;
	output_cacetinhodearrasto.open("output_cacetinhodearrasto.txt");

	//calculo de sustentação ao longo da envergadura

	double i = 0;
	double CARGAAA = 0;
	double MOMENTOO = 0;
	double x = 0;
	double car = 0;
	double car2 =0;
	double tinho = f;
    double sominha = 0;
    double somona = 0;

	while (f<(envergadura+0.1)){
		//double croc = envergadura -
		//double crocm = -1*croc;
		double midi = (i+f)/2;
		double a1 = midi*m1 + cordaponta;
		double a2 = midi*m2 + hingeponta;
		double a3 = midi*m3 + condapontaEH;
		double j = 0.95;
		double range = 0.1;
		double e = a1/10;
		double ih = a1 - a2;
		double trucao;
		double arco;
        sominha = 0;
        somona = 0;
		arco = 0;
		while(j>(0.0)){
			x = a3-(a3-j*a1);
			trucao = 3*supcarga*(pow(((a3-(a3-j*a1))/a1),2));
			car = trucao*(e*tinho);
			car2 = trucao*(e*f);
			sominha = sominha + car2;
			arco = car*(x-ih);
			somona = somona + arco;
			j = j-range;
            cpcacetinho(car);
		}

		CARGAAA = sominha/f;
		MOMENTOO = somona;

        output_cacetinhodearrasto << i*0.3048 << "    " << CARGAAA*14.584 << "    " << MOMENTOO*4.4452 << "\n";

		i = f;
		f = tinho + f;
	}

	output_cacetinhodearrasto.close();

}


void junqueira(double n1, double WSm, double WSmin, double Vasel, double Vamin, double Vcsel, double Vcmin){

	//calculo de cargas para o TAB, FLAP e aileron

	double olho1 = n1*WSm;
	double olho2 = n1*WSmin;
	double TAB = 0.78*olho1;
	double FLAP = 0.64*olho1;
	double aileron = 0.466*olho1;

	double fc;
	double fc1 = pow((Vasel/Vamin),2);
	double fc2 = pow((Vcsel/Vcmin),2);

	if(fc1>fc2){
		fc = fc1;
	}
	else{
		fc = fc2;
	}

	aileron1(fc, aileron);
	TAB1(fc, TAB);
	FLAP1(fc, FLAP);

}


void aileron1(double fc, double aileron){

	//calculo de cargas para o aileron

    ifstream i_aileron;
	double cordaponta, cordaraiz, hingeponta, hingeraiz, envergadura;
	string linha;
    i_aileron.open("i_aileron.txt");
    getline(i_aileron,linha);
    stringstream geek(linha);
    geek >> cordaponta;
	getline(i_aileron,linha);
    stringstream geek2(linha);
    geek2 >> cordaraiz;
	getline(i_aileron,linha);
    stringstream geek3(linha);
    geek3 >> hingeponta;
	getline(i_aileron,linha);
    stringstream geek4(linha);
    geek4 >> hingeraiz;
	getline(i_aileron,linha);
    stringstream geek5(linha);
    geek5 >> envergadura;

    cordaponta = cordaponta*3.28084;
    cordaraiz =  cordaraiz*3.28084;
	hingeponta = hingeponta*3.28084;
	hingeraiz =  hingeraiz*3.28084;
	envergadura =  envergadura*3.28084;

	double area = envergadura*(cordaponta+cordaraiz)/2;
	double carga = fc*aileron;
    ofstream output_ail;

	output_ail.open("output_ail.txt");

	//cout << "carregamento total no Aileron:" << "  " << area*carga*4.4452 << " " << "N" << endl;
    output_ail << "carregamento total no Aileron:" << "  " << area*carga*4.4452 << " " << "N" << endl;

    output_ail.close();


	supasa(envergadura, area, carga, envergadura, cordaraiz, cordaponta, hingeraiz, hingeponta);


}

void TAB1(double fc, double TAB){

	//calculo de cargas para o TAB

    ifstream i_TAB;
	double cordaponta, cordaraiz, hingeponta, hingeraiz, envergadura;
	string linha;
    i_TAB.open("i_TAB.txt");
    getline(i_TAB,linha);
    stringstream geek(linha);
    geek >> cordaponta;
	getline(i_TAB,linha);
    stringstream geek2(linha);
    geek2 >> cordaraiz;
	getline(i_TAB,linha);
    stringstream geek3(linha);
    geek3 >> hingeponta;
	getline(i_TAB,linha);
    stringstream geek4(linha);
    geek4 >> hingeraiz;
	getline(i_TAB,linha);
    stringstream geek5(linha);
    geek5 >> envergadura;

    cordaponta = cordaponta*3.28084;
    cordaraiz =  cordaraiz*3.28084;
	hingeponta = hingeponta*3.28084;
	hingeraiz =  hingeraiz*3.28084;
	envergadura =  envergadura*3.28084;


	double area = envergadura*(cordaponta+cordaraiz)/2;
	double carga = fc*TAB;

	//cout << "carregamento total no TAB:" << "  " << area*carga*4.4452 << " " << "N" << endl;

    double f = envergadura/30;
	double fac = area/envergadura;
	double m1 = (cordaraiz-cordaponta)/envergadura;
	double m2 = (hingeraiz - hingeponta)/envergadura;

	TABFLAP(f,fac,m1,m2,carga,hingeponta,cordaponta,envergadura, area);

}

void FLAP1(double fc, double FLAP){

	//calculo de cargas para o FLAP

    ifstream i_FLAP;
	double cordaponta, cordaraiz, hingeponta, hingeraiz, envergadura;
	string linha;
    i_FLAP.open("i_FLAP.txt");


    getline(i_FLAP,linha);
    stringstream geek(linha);
    geek >> cordaponta;

	getline(i_FLAP,linha);
    stringstream geek2(linha);
    geek2 >> cordaraiz;
	getline(i_FLAP,linha);
    stringstream geek3(linha);
    geek3 >> hingeponta;
	getline(i_FLAP,linha);
    stringstream geek4(linha);
    geek4 >> hingeraiz;
	getline(i_FLAP,linha);
    stringstream geek5(linha);
    geek5 >> envergadura;

    cordaponta = cordaponta*3.28084;
    cordaraiz =  cordaraiz*3.28084;
	hingeponta = hingeponta*3.28084;
	hingeraiz =  hingeraiz*3.28084;
	envergadura =  envergadura*3.28084;

	double area = envergadura*(cordaponta+cordaraiz)/2;
	double carga = fc*FLAP;

	//cout << "carregamento total no FLAP:" << "  " << area*carga*4.4452 << " " << "N" << endl;

    double f = envergadura/30;
	double fac = area/envergadura;
	double m1 = (cordaraiz-cordaponta)/envergadura;
	double m2 = (hingeraiz - hingeponta)/envergadura;

	FLAPTAB(f,fac,m1,m2,carga,hingeponta,cordaponta,envergadura, area);

}

void supasa(double evnergadura, double area, double carga, double envergadura, double cordaraiz, double cordaponta, double hingeraiz, double hingeponta){

	//calculo de coef geométricos de sups de controle

	double f = envergadura/30;
	double fac = area/envergadura;
	double m1 = (cordaraiz-cordaponta)/envergadura;
	double m2 = (hingeraiz - hingeponta)/envergadura;

	calculaemp1(f,fac,m1,m2,carga,hingeponta,cordaponta,envergadura, area);

}

void TABFLAP(double f, double fac, double m1, double m2, double carga, double hingeponta, double cordaponta, double envergadura, double area){

    ofstream output_TAB;
    output_TAB.open("output_TAB.txt");

	//calculo de distribuição de cargas ao longo da envergadura e corda

	double midi, a1, a2, aa1, aa2, c1, c11, c22, c2,c3,c4, M1, M2, m3, m4, c5, m5, CARGAAAA, MOMENTOOO;
	double i =0;
	double clovis = 0;
	double tinho = f;

	m4 = 0;
	while (f<(envergadura+0.1)){
		midi = (i+f)/2;
		a1 = midi*m1 + cordaponta;
		a2 = midi*m2 + hingeponta;
		aa1 = a2*tinho;
		aa2 = (a1-a2)*tinho;
		c1 = aa1;
		c2 = aa2*carga;
		c3 = c1+c2;
        clovis = clovis + c3;
        i = f;
		f = tinho + f;
	}
    f = tinho;
    tinho = f;
    i = 0;

	fac = area/clovis;

		while (f<(envergadura+0.1)){
		midi = (i+f)/2;
		a1 = midi*m1 + cordaponta;
		a2 = midi*m2 + hingeponta;
		aa1 = a2*tinho;
		aa2 = (a1-a2)*tinho;
		c1 = aa1;
		c2 = aa2*carga;
		c3 = c1+c2;
		c11 = c1*fac;
		c22 = c2*fac;
		c4 = c3 *fac;
		M1 = c11*a2/2;
		M2 = -(((c4/3)*a1/3)+((2*c4/3)*a1/2));
		m3 = M1+M2;
		m4 = m4 + m3;
		c5 = c4*carga;
		m5=m3*carga;
		CARGAAAA = c5/tinho;
		MOMENTOOO = m5/tinho;

        output_TAB << i*0.3048 << "    " << CARGAAAA*14.584 << "    "  << MOMENTOOO*4.4452 << "    " << -0.25*CARGAAAA*14.584 << "    " << -0.25*MOMENTOOO*4.4452 <<"\n";

		i = f;
		f = tinho + f;
	}

    output_TAB.close();


}

void FLAPTAB(double f, double fac, double m1, double m2, double carga, double hingeponta, double cordaponta, double envergadura, double area){

	ofstream output_FLAP;

	output_FLAP.open("output_FLAP.txt");

	//calculo de distribuição de cargas ao longo da envergadura e corda

	double midi, a1, a2, aa1, aa2, c1, c11, c22, c2,c3,c4, M1, M2, m3, m4, c5, m5, CARGAAAA, MOMENTOOO;
	double i =0;
	double clovis = 0;
	double tinho = f;

	m4 = 0;
	while (f<(envergadura+0.1)){
		midi = (i+f)/2;
		a1 = midi*m1 + cordaponta;
		a2 = midi*m2 + hingeponta;
		aa1 = a2*tinho;
		aa2 = (a1-a2)*tinho;
		c1 = aa1;
		c2 = aa2*carga;
		c3 = c1+c2;
        clovis = clovis + c3;
        i = f;
		f = tinho + f;
	}
    f = tinho;
    tinho = f;
    i = 0;

	fac = area/clovis;

		while (f<(envergadura+0.1)){
		midi = (i+f)/2;
		a1 = midi*m1 + cordaponta;
		a2 = midi*m2 + hingeponta;
		aa1 = a2*tinho;
		aa2 = (a1-a2)*tinho;
		c1 = aa1;
		c2 = aa2*carga;
		c3 = c1+c2;
		c11 = c1*fac;
		c22 = c2*fac;
		c4 = c3 *fac;
		M1 = c11*a2/2;
		M2 = -(((c4/3)*a1/3)+((2*c4/3)*a1/2));
		m3 = M1+M2;
		m4 = m4 + m3;
		c5 = c4*carga;
		m5=m3*carga;
		CARGAAAA = c5/tinho;
		MOMENTOOO = m5/tinho;

        output_FLAP << i*0.3048 << "    " << CARGAAAA*14.584 << "    "  << MOMENTOOO*4.4452 << "    " << -0.25*CARGAAAA*14.584 << "    " << -0.25*MOMENTOOO*4.4452<< "\n";
		i = f;
		f = tinho + f;
	}

	output_FLAP.close();

}

void calculaemp1(double f, double fac, double m1, double m2, double carga, double hingeponta, double cordaponta, double envergadura, double area){

    ofstream output_aileron;
	output_aileron.open("output_aileron.txt");

	//calculo de distribuição de cargas ao longo da envergadura e corda

	double midi, a1, a2, aa1, aa2, c1, c11, c22, c2,c3,c4, M1, M2, m3, m4, c5, m5, CARGAAAA, MOMENTOOO;
	double i =0;
	double GIZ = 0;
	double tinho = f;

	m4 = 0;
	while (f<(envergadura+0.1)){
		midi = (i+f)/2;
		a1 = midi*m1 + cordaponta;
		a2 = midi*m2 + hingeponta;
		aa1 = a2*tinho;
		aa2 = (a1-a2)*tinho;
		c1 = aa1;
		c2 = c2 = aa2/2;
		c3 = c1+c2;
        GIZ = GIZ + c3;
        i = f;
		f = tinho + f;

	}
    f = tinho;
    i = 0;
	fac = area/GIZ;

		while (f<(envergadura+0.1)){
		midi = (i+f)/2;
		a1 = midi*m1 + cordaponta;
		a2 = midi*m2 + hingeponta;
		aa1 = a2*tinho;
		aa2 = (a1-a2)*tinho;
		c1 = aa1;
		c2 = c2 = aa2/2;
		c3 = c1+c2;
		c11 = c1*fac;
		c22 = c2*fac;
		c4 = c3 * fac;
		M1 = c11*a2/2;
		M2 = -(a1-a2)/3*c22;
		m3 = M1+M2;
		m4 = m4 + m3;
		c5 = c4*carga;
		m5=m3*carga;
		CARGAAAA = c5/tinho;
		MOMENTOOO = m5/tinho;
		output_aileron << i*0.3048 << "    " << CARGAAAA*14.584 << "    "  << MOMENTOOO*4.4452 << "\n";
		i = f;
		f = tinho + f;
        }
    output_aileron.close();
}


void limpa1(double car){
    ofstream output_cp_profundor;
	output_cp_profundor.open("output_cp_profundor.txt");
	output_cp_profundor << "";
	output_cp_profundor.close();

}

void limpa2(double car){
    ofstream output_cp_cacetinho;
	output_cp_cacetinho.open("output_cp_cacetinho.txt");
	output_cp_cacetinho << "";
	output_cp_cacetinho.close();
}


void cpprofundor(double car){
    ofstream output_cp_profundor;
	output_cp_profundor.open("output_cp_profundor.txt",ios::app);

	output_cp_profundor << car*47.88 << "    ";
    cp1 = cp1 +1;
	if (cp1>9){
        output_cp_profundor << "\n";
        cp1=0;
	}
	output_cp_profundor.close();

}

void cpcacetinho(double car){
    ofstream output_cp_cacetinho;
	output_cp_cacetinho.open("output_cp_cacetinho.txt",ios::app);

	output_cp_cacetinho << car*47.88 << "    ";
    cp2 = cp2 + 1;
	if (cp2>9){
        output_cp_cacetinho << "\n";
        cp2=0;
	}
	output_cp_cacetinho.close();
}


void cp(double ro, double vmax){

    ifstream dados_nervura;
    ifstream dados_intradorso;
    ifstream dados_extradorso;
    double cp, g;

    double access[4];
	string linha;
	int gertrudes = 0;
    ofstream output_cpextradorso;
    ofstream output_cpintradorso;

	output_cpextradorso.open("output_cpextradorso.txt");
	output_cpintradorso.open("output_cpintradorso.txt");


	dados_nervura.open("dados_nervura.txt");
    dados_extradorso.open("dados_extradorso.txt");
    dados_intradorso.open("dados_intradorso.txt");


    for(int p=0; p<5; p++){
        getline(dados_nervura,linha);
        stringstream alicate(linha);
        alicate >> access[p];

    }

    double espessura = access[0];
    double distancia = access[1];
    double comprimentointra = access [2];
    double comprimentoextra = access [3];
    double velocidadeAnalise = access [4];

    while(getline(dados_extradorso,linha)){
        stringstream bufa(linha);
        bufa >> cp;
        g = cpaolongodoperfil(espessura, distancia, comprimentoextra, cp, ro, velocidadeAnalise);
        output_cpextradorso << g << "\n";

    }

    while(getline(dados_intradorso,linha)){
        stringstream ko(linha);
        ko >> cp;
        g = cpaolongodoperfil(espessura, distancia, comprimentointra, cp, ro, velocidadeAnalise);
        output_cpintradorso << g << "\n";

    }

}

double cpaolongodoperfil(double espessura, double distancia, double comprimento,double cp, double ro, double velocidadeAnalise){

	double a = cp*0.5*ro*(pow(velocidadeAnalise,2));

	double area1 = comprimento*distancia;
	double area2 = comprimento*espessura;
	double area3 = area1/area2;

	double cudeborboleta = area3*a; //p-pinf;

	return cudeborboleta;
}
