import { useState } from "react";
import { motion } from "framer-motion";
import { Section } from "./components/Section";

const navItems = [
  { id: "inicio", label: "Inicio" },
  { id: "diagnostico", label: "Diagnóstico" },
  { id: "roadmap", label: "Hoja de Ruta" },
  { id: "roi", label: "ROI & Inversión" },
  { id: "equipo", label: "Equipo" },
  { id: "proximos-pasos", label: "Próximos pasos" }
];

function scrollTo(id: string) {
  const el = document.getElementById(id);
  if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
}

export default function App() {
  const [hoursPerDay, setHoursPerDay] = useState(3);
  const [hourlyCost, setHourlyCost] = useState(10);
  const [employees, setEmployees] = useState(2);

  const weeklySavings = hoursPerDay * employees * hourlyCost * 5;
  const monthlySavings = weeklySavings * 4.33;
  const yearlySavings = monthlySavings * 12;

  return (
    <div className="min-h-screen bg-gradient-to-b from-quai-navy via-slate-950 to-slate-900 text-slate-50">
      {/* Top nav */}
      <header className="sticky top-0 z-40 border-b border-slate-800/80 bg-quai-navy/90 backdrop-blur">
        <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-3">
          <div className="flex items-center gap-2">
            <img
              src="/quai_analytics_logo.png"
              alt="QuAI Analytics"
              className="h-9 w-auto"
            />
            <div>
              <p className="text-sm font-semibold tracking-wide">
                QuAI Analytics
              </p>
              <p className="text-[11px] text-slate-400">
                Estrategia de IA & Analítica
              </p>
            </div>
          </div>
          <nav className="hidden gap-5 text-xs md:flex">
            {navItems.map((item) => (
              <button
                key={item.id}
                onClick={() => scrollTo(item.id)}
                className="text-slate-300 hover:text-quai-teal transition-colors"
              >
                {item.label}
              </button>
            ))}
          </nav>
        </div>
      </header>

      {/* Hero */}
      <Section
        id="inicio"
        eyebrow="Propuesta Digital"
        title="De datos dispersos a decisiones en tiempo real para El Alandalus."
        description="Propuesta de valor de QuAI Analytics para transformar la gestión operativa y financiera de El Alandalus mediante analítica avanzada, BI y automatización con IA."
        dark
      >
        <div className="grid gap-10 md:grid-cols-[3fr,2fr] md:items-center">
          <div>
            <motion.p
              initial={{ opacity: 0, y: 16 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.1, duration: 0.5 }}
              className="text-lg text-slate-200 mb-6"
            >
              Hoy, sus números viven en Excel, reportes manuales y la computadora
              de &quot;Caja Menuda&quot;. Nuestra propuesta conecta esas piezas,
              las limpia y las convierte en un panel vivo de ventas, costos y
              rentabilidad.
            </motion.p>
            <div className="flex flex-wrap gap-3">
              <button
                onClick={() => scrollTo("proximos-pasos")}
                className="rounded-full bg-quai-teal px-5 py-2.5 text-sm font-semibold text-slate-950 shadow-lg shadow-quai-teal/40 hover:bg-quai-teal/90 transition-colors"
              >
                Agendar reunión de 30 min
              </button>
              <button
                onClick={() => scrollTo("diagnostico")}
                className="rounded-full border border-slate-700 px-5 py-2.5 text-sm font-semibold text-slate-100 hover:border-quai-teal hover:text-quai-teal transition-colors"
              >
                Ver diagnóstico actual
              </button>
            </div>
            <div className="mt-6 flex flex-wrap gap-6 text-xs text-slate-400">
              <div>
                <p className="font-semibold text-slate-200">
                  +10 años manejando datos
                </p>
                <p>Implementaciones de analítica y BI en distintos sectores.</p>
              </div>
              <div>
                <p className="font-semibold text-slate-200">
                  Foco en negocio
                </p>
                <p>No solo modelos: decisiones y ahorro de horas-hombre.</p>
              </div>
            </div>
          </div>
          <motion.div
            initial={{ opacity: 0, scale: 0.96, y: 12 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            transition={{ delay: 0.15, duration: 0.5 }}
            className="rounded-2xl border border-slate-800 bg-slate-900/70 p-5 shadow-2xl"
          >
            <p className="text-xs font-semibold uppercase tracking-wide text-quai-teal mb-3">
              Radiografía en 30 segundos
            </p>
            <ul className="space-y-3 text-sm text-slate-200">
              <li>
                🛑 <strong>Ceguera operativa:</strong> reportes dependen de
                digitación manual en el ERP.
              </li>
              <li>
                ⏱️ <strong>2–3 horas diarias</strong> del equipo administrativo
                se pierden en transcribir facturas.
              </li>
              <li>
                📂 <strong>Datos aislados:</strong> información crítica atrapada
                en PC locales y hojas de cálculo.
              </li>
            </ul>
            <div className="mt-4 rounded-xl bg-slate-950/70 px-4 py-3 text-xs text-slate-300 border border-slate-800">
              <p>
                Nuestra propuesta conecta su ERP mediante VPN segura, automatiza
                la ingesta de datos y despliega dashboards listos para tomar
                decisiones, con un módulo opcional de OCR para eliminar la
                digitación manual.
              </p>
            </div>
          </motion.div>
        </div>
      </Section>

      {/* Diagnóstico */}
      <Section
        id="diagnostico"
        eyebrow="1 · Diagnóstico"
        title="Dónde está hoy El Alandalus y qué está costando no actuar."
      >
        <div className="grid gap-8 md:grid-cols-2">
          <div className="rounded-2xl border border-red-900/60 bg-gradient-to-br from-red-950 via-slate-950 to-slate-950 p-6">
            <h3 className="text-lg font-semibold mb-3">La situación actual</h3>
            <ul className="space-y-3 text-sm text-slate-200">
              <li>
                • Reportes financieros y operativos dependen de{" "}
                <strong>carga manual de datos</strong>.
              </li>
              <li>
                • Cierre de mes y control de costos toman{" "}
                <strong>días de trabajo</strong>.
              </li>
              <li>
                • Los socios no tienen una vista consolidada y en tiempo casi
                real del negocio.
              </li>
            </ul>
          </div>
          <div className="rounded-2xl border border-emerald-900/60 bg-gradient-to-br from-emerald-950 via-slate-950 to-slate-950 p-6">
            <h3 className="text-lg font-semibold mb-3">La oportunidad</h3>
            <ul className="space-y-3 text-sm text-slate-200">
              <li>
                • Automatizar la conexión al ERP mediante{" "}
                <strong>VPN segura</strong> sin cambiar el software actual.
              </li>
              <li>
                • Construir dashboards de ventas y costos que se{" "}
                <strong>actualizan solos</strong>.
              </li>
              <li>
                • Activar un módulo de <strong>OCR + IA</strong> para que las
                facturas se lean y se preparen solas para el sistema.
              </li>
            </ul>
          </div>
        </div>
      </Section>

      {/* Roadmap */}
      <Section
        id="roadmap"
        eyebrow="2 · Hoja de Ruta"
        title="Un camino por fases, con valor en cada etapa."
        description="Proponemos una implementación gradual que reduce riesgo, genera confianza en el equipo y entrega resultados visibles desde el primer mes."
      >
        <div className="grid gap-6 md:grid-cols-3">
          {[
            {
              fase: "Fase 1",
              titulo: "Conexión segura",
              detalle:
                "VPN y permisos de solo lectura al ERP. Validación de seguridad y pruebas de conexión.",
              tiempo: "Semana 1"
            },
            {
              fase: "Fase 2",
              titulo: "Datos listos",
              detalle:
                "Modelado y limpieza de datos de ventas y costos. Pipelines automáticos de actualización.",
              tiempo: "Semanas 1–2"
            },
            {
              fase: "Fase 3",
              titulo: "Dashboards de decisión",
              detalle:
                "Tableros de ventas, costos y rentabilidad accesibles desde web y móvil.",
              tiempo: "Semana 3"
            },
            {
              fase: "Fase 4",
              titulo: "Automatización (OCR)",
              detalle:
                "Módulo IA para lectura de facturas y propuesta de asientos en el sistema.",
              tiempo: "Semana 4"
            },
            {
              fase: "Fase 5",
              titulo: "Capacitación",
              detalle:
                "Entrenamiento al equipo, manual de uso y acompañamiento del lanzamiento.",
              tiempo: "Semana 5 en adelante"
            }
          ].map((item, idx) => (
            <motion.div
              key={item.fase}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.3 }}
              transition={{ delay: idx * 0.05, duration: 0.4 }}
              className="rounded-2xl border border-slate-800 bg-slate-950/60 p-5"
            >
              <p className="text-xs font-semibold tracking-wide text-quai-teal uppercase mb-1">
                {item.fase}
              </p>
              <h3 className="text-base font-semibold mb-2">{item.titulo}</h3>
              <p className="text-xs text-slate-300 mb-3">{item.detalle}</p>
              <p className="inline-flex rounded-full bg-slate-900 px-3 py-1 text-[11px] text-slate-300 border border-slate-700">
                ⏱ {item.tiempo}
              </p>
            </motion.div>
          ))}
        </div>
      </Section>

      {/* ROI */}
      <Section
        id="roi"
        eyebrow="3 · ROI & Inversión"
        title="Cuánto puede ahorrar El Alandalus al automatizar su operación."
      >
        <div className="grid gap-8 md:grid-cols-[2fr,3fr] md:items-start">
          <div className="space-y-4 text-sm text-slate-200">
            <p>
              Nuestra experiencia muestra que eliminar la digitación manual y
              mejorar la visibilidad puede ahorrar decenas de horas al mes y
              reducir errores humanos costosos.
            </p>
            <p>
              A continuación puedes ajustar las variables clave (horas diarias
              ahorradas, costo por hora y número de personas) para estimar el
              impacto económico anual de la solución.
            </p>
            <ul className="space-y-2">
              <li>
                • Ahorro en horas-hombre de digitación y armado de reportes.
              </li>
              <li>
                • Menos errores contables y mejor control de ITBMS y costos.
              </li>
              <li>• Decisiones más rápidas sobre menú, precios y promociones.</li>
            </ul>
          </div>
          <div className="rounded-2xl border border-slate-800 bg-slate-950/70 p-6 text-sm">
            <h3 className="text-base font-semibold mb-4">
              Calculadora rápida de ahorro
            </h3>
            <div className="space-y-4">
              <div>
                <div className="flex items-center justify-between text-xs mb-1">
                  <span>Horas diarias ahorradas</span>
                  <span className="font-semibold text-quai-teal">
                    {hoursPerDay.toFixed(1)} h/día
                  </span>
                </div>
                <input
                  type="range"
                  min={0.5}
                  max={8}
                  step={0.5}
                  value={hoursPerDay}
                  onChange={(e) => setHoursPerDay(Number(e.target.value))}
                  className="w-full accent-quai-teal"
                />
              </div>
              <div>
                <div className="flex items-center justify-between text-xs mb-1">
                  <span>Costo por hora del trabajador (USD)</span>
                  <span className="font-semibold text-quai-teal">
                    ${hourlyCost.toFixed(0)}
                  </span>
                </div>
                <input
                  type="range"
                  min={5}
                  max={50}
                  step={1}
                  value={hourlyCost}
                  onChange={(e) => setHourlyCost(Number(e.target.value))}
                  className="w-full accent-quai-teal"
                />
              </div>
              <div>
                <div className="flex items-center justify-between text-xs mb-1">
                  <span>Número de personas impactadas</span>
                  <span className="font-semibold text-quai-teal">
                    {employees}
                  </span>
                </div>
                <input
                  type="range"
                  min={1}
                  max={20}
                  step={1}
                  value={employees}
                  onChange={(e) => setEmployees(Number(e.target.value))}
                  className="w-full accent-quai-teal"
                />
              </div>
              <div className="mt-2 space-y-1 text-slate-200">
                <p>
                  • Ahorro semanal estimado:{" "}
                  <span className="font-semibold">
                    ${weeklySavings.toLocaleString(undefined, { maximumFractionDigits: 0 })}
                  </span>
                </p>
                <p>
                  • Ahorro mensual (4.33 semanas):{" "}
                  <span className="font-semibold">
                    $
                    {monthlySavings.toLocaleString(undefined, {
                      maximumFractionDigits: 0
                    })}
                  </span>
                </p>
                <p>
                  • Ahorro anual estimado:{" "}
                  <span className="font-semibold text-quai-teal">
                    $
                    {yearlySavings.toLocaleString(undefined, {
                      maximumFractionDigits: 0
                    })}
                  </span>
                </p>
              </div>
              <p className="mt-2 text-[11px] text-slate-400">
                Los valores son solo una guía. En la reunión afinamos los
                supuestos con datos reales de El Alandalus para construir el
                caso de negocio definitivo.
              </p>
            </div>
          </div>
        </div>
      </Section>

      {/* Equipo */}
      <Section
        id="equipo"
        eyebrow="4 · Equipo"
        title="Quién te acompaña en esta transformación."
      >
        <div className="grid gap-6 md:grid-cols-2">
          <div className="rounded-2xl border border-slate-800 bg-slate-950/70 p-5">
            <h3 className="text-base font-semibold mb-1">Ing. Ricardo Álvarez</h3>
            <p className="text-xs text-quai-teal mb-3">
              MSc, Científico de Datos – Fundador de QuAI Analytics
            </p>
            <p className="text-sm text-slate-200">
              Experto en analítica avanzada de datos y gestión estratégica de
              negocios. Lidera el diseño de la solución, priorización de
              indicadores clave y asegura que la implementación responda a los
              objetivos reales de El Alandalus.
            </p>
          </div>
          <div className="rounded-2xl border border-slate-800 bg-slate-950/70 p-5">
            <h3 className="text-base font-semibold mb-1">
              Ing. Alexander Cuadra
            </h3>
            <p className="text-xs text-quai-teal mb-3">
              Ingeniero de Datos – QuAI Analytics
            </p>
            <p className="text-sm text-slate-200">
              Especialista en ingeniería de datos e integración de sistemas. Se
              enfoca en conectar el ERP, estructurar la base de datos en la
              nube y garantizar que los dashboards sean robustos y confiables.
            </p>
          </div>
        </div>
      </Section>

      {/* Próximos pasos */}
      <Section
        id="proximos-pasos"
        eyebrow="5 · Próximos pasos"
        title="Si esto hace sentido, el siguiente paso es muy simple."
        description="Proponemos una reunión remota de 30 minutos para revisar esta propuesta, adaptar tiempos y paquetes al contexto actual de El Alandalus y definir una fecha tentativa de inicio."
        dark
      >
        <div className="grid gap-6 md:grid-cols-[3fr,2fr] md:items-center">
          <div className="space-y-3 text-sm text-slate-200">
            <p>En esa conversación podemos:</p>
            <ul className="space-y-2">
              <li>• Confirmar el alcance técnico (VPN, acceso a ERP, usuarios).</li>
              <li>• Ajustar los dashboards prioritarios para socios y gerencia.</li>
              <li>• Alinear inversión, plazos y modalidad de soporte mensual.</li>
            </ul>
            <p>
              Si después de la llamada ambas partes ven encaje, avanzamos a
              formalizar el acuerdo y calendarizar la Fase 1.
            </p>
          </div>
          <div className="rounded-2xl border border-quai-teal/40 bg-slate-950/80 p-5 text-sm">
            <p className="text-xs font-semibold uppercase tracking-wide text-quai-teal mb-2">
              Contacto
            </p>
            <p className="text-slate-100 font-semibold mb-1">
              QuAI Analytics
            </p>
            <p className="text-slate-300 mb-2">
              info@quaianalytics.com · (+507) 6679‑1845
            </p>
            <p className="text-xs text-slate-400 mb-4">
              Sitio: QuAIAnalytics.com (puedes enlazar aquí tu web, LinkedIn o
              Calendly real).
            </p>
            <button className="w-full rounded-full bg-quai-teal px-4 py-2.5 text-sm font-semibold text-slate-950 shadow-lg shadow-quai-teal/40 hover:bg-quai-teal/90 transition-colors">
              Agendar reunión de 30 minutos
            </button>
          </div>
        </div>
        <p className="mt-6 text-[11px] text-slate-500">
          © {new Date().getFullYear()} QuAI Analytics. Propuesta confidencial,
          preparada exclusivamente para El Alandalus.
        </p>
      </Section>
    </div>
  );
}


