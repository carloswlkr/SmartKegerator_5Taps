#ifndef FLOWMETERMANAGER_H
#define FLOWMETERMANAGER_H

#include <QApplication>
#include <QProcess>
#include <QTimer>
#include <QObject>


using namespace std;

enum BeerTapSide { LEFT_TAP, IZQ_CENTRO_TAP, CENTER_TAP, DER_CENTRO_TAP, RIGHT_TAP };

class Keg;

class FlowMeterManager : public QObject
{
    Q_OBJECT
public:
    static FlowMeterManager* Instance;

    static Keg *CurrentKeg;
    static BeerTapSide CurrentTapSide;
    static double LastTickAt;
    static int Ticks;
    static bool IsPouring;
    static bool ConflictingTicks;

    static void Init();
    static void Shutdown();
    void FinishPour();

    FlowMeterManager();

signals:
    void PourStarted();
    void FlowMeterTicked();
    void PourFinished();

private slots:
    void onFlowMeterData();
    void onUpdateTick();

private:
    void beginPour(BeerTapSide);

    int flowMeterPinLeft;
    int flowMeterPinIzqCentro;
    int flowMeterPinCenter;
    int flowMeterPinDerCentro;
    int flowMeterPinRight;

    string gpioWFICommand;
    QString leftTickString, izqCentroTickString, centerTickString, derCentroTickString, rightTickString;
    QProcess* gpioProc;
    QTimer updateTimer;

};

#endif // FLOWMETERMANAGER_H
