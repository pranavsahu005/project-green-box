import React from 'react';

const Analytics: React.FC = () => {
  return (
    <div className="analytics-page p-10">
      <h1 className="text-4xl font-instrument-serif">Deep Learning Analytics</h1>
      <div className="grid grid-cols-2 gap-4 mt-10">
        <div className="stat-card p-6 bg-white rounded-xl shadow-lg">
          <span className="text-slate-400">Yield Forecast</span>
          <div className="text-3xl font-bold">+42.8%</div>
        </div>
        <div className="stat-card p-6 bg-white rounded-xl shadow-lg">
          <span className="text-slate-400">Carbon Sequestration</span>
          <div className="text-3xl font-bold">12.4t CO2e</div>
        </div>
      </div>
    </div>
  );
};

export default Analytics;
 <p className="text-slate-500">Intelligent automation for precision reforestation.</p>
          </header>
          
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
            <div className="lg:col-span-2 bg-white rounded-3xl p-6 shadow-sm border border-slate-200">
              <h2 className="text-lg font-semibold mb-6">Photosynthesis Activity</h2>
              <GrowthChart type="linear" data="photosynthesis" />
            </div>
            <div className="bg-white rounded-3xl p-6 shadow-sm border border-slate-200">
              <h2 className="text-lg font-semibold mb-6">Environment Score</h2>
              <TelemetryPanel mode="environment" />
            </div>
          </div>
        </main>
      </div>
    </div>
  );
};

export default Dashboard;
